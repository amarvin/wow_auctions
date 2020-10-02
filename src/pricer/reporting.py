"""Produces reporting to help interpret analysis and campaigns."""
import logging

from pricer import config as cfg

logger = logging.getLogger(__name__)


def have_in_bag() -> None:
    """Prints expected profits, make sure its in your bag."""
    sell_policy = cfg.reader("outputs", "sell_policy", "parquet")
    sell_policy = sell_policy.set_index("item")

    sell_policy = sell_policy[
        sell_policy["estimated_profit"] > sell_policy["feasible_profit"]
    ]

    print(sell_policy["estimated_profit"])
