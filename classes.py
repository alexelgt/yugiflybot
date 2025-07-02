# Bots Common Code
# Copyright (C) 2025 Alexelgt

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio

import contextlib

from collections.abc import Coroutine

from typing import Any, Callable, Optional, Union

from telegram.ext import AIORateLimiter

from telegram._utils.types import JSONDict

from telegram.error import RetryAfter

from telegram._utils.logging import get_logger

_LOGGER = get_logger(__name__ + "._aioratelimiter", class_name="CustomAIORateLimiter")


class CustomAIORateLimiter(AIORateLimiter):
    async def process_request(
        self,
        callback: Callable[..., Coroutine[Any, Any, Union[bool, JSONDict, list[JSONDict]]]],
        args: Any,
        kwargs: dict[str, Any],
        endpoint: str,  # noqa: ARG002
        data: dict[str, Any],
        rate_limit_args: Optional[int],
    ) -> Union[bool, JSONDict, list[JSONDict]]:
        """
        Processes a request by applying rate limiting.

        See :meth:`telegram.ext.BaseRateLimiter.process_request` for detailed information on the
        arguments.

        Args:
            rate_limit_args (:obj:`None` | :obj:`int`): If set, specifies the maximum number of
                retries to be made in case of a :exc:`~telegram.error.RetryAfter` exception.
                Defaults to :paramref:`AIORateLimiter.max_retries`.
        """
        max_retries = rate_limit_args or self._max_retries

        group: Union[int, str, bool] = False
        chat: bool = False
        chat_id = data.get("chat_id")
        allow_paid_broadcast = data.get("allow_paid_broadcast", False)
        if chat_id is not None:
            chat = True

        # In case user passes integer chat id as string
        with contextlib.suppress(ValueError, TypeError):
            chat_id = int(chat_id)  # type: ignore[arg-type]

        if (isinstance(chat_id, int) and chat_id < 0) or isinstance(chat_id, str):
            # string chat_id only works for channels and supergroups
            # We can't really tell channels from groups though ...
            group = chat_id

        for i in range(max_retries + 1):
            try:
                return await self._run_request(
                    chat=chat,
                    group=group,
                    allow_paid_broadcast=allow_paid_broadcast,
                    callback=callback,
                    args=args,
                    kwargs=kwargs,
                )
            except RetryAfter as exc:
                if i == max_retries:
                    _LOGGER.exception(
                        "Rate limit hit in chat_id %d after maximum of %d retries", chat_id, max_retries, exc_info=exc
                    )
                    raise

                sleep = exc._retry_after.total_seconds() + 0.1  # pylint: disable=protected-access
                _LOGGER.info("Rate limit hit in chat_id %d. Retrying after %f seconds", chat_id, sleep)
                # Make sure we don't allow other requests to be processed
                # self._retry_after_event.clear()
                await asyncio.sleep(sleep)
            # finally:
            #     # Allow other requests to be processed
            #     self._retry_after_event.set()
        return None  # type: ignore[return-value]
