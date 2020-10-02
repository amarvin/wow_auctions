"""Tests for source.py."""
from numpy import nan
import pandas as pd

from pricer import sources


def test_item_skeleton() -> None:
    """It tests nothing useful."""
    example = {
        "Elixir of the Mongoose": {
            "min_holding": nan,
            "max_holding": 60,
            "max_sell": nan,
            "Buy": nan,
            "Sell": True,
            "made_from": {
                "Crystal Vial": 1,
                "Mountain Silversage": 2,
                "Plaguebloom": 2,
            },
            "make_pass": nan,
            "vendor_price": nan,
        },
        "Sungrass": {
            "min_holding": nan,
            "max_holding": 100,
            "max_sell": nan,
            "Buy": True,
            "Sell": True,
            "made_from": nan,
            "make_pass": nan,
            "vendor_price": nan,
        },
    }
    example_df = pd.DataFrame.from_dict(example, orient="index")
    sources.process_item_skeleton(example_df)


def test_auctioneer_data() -> None:
    """It tests nothing useful."""
    example = {
        26759: {
            0: 'r\\"',
            1: "46",
            2: "4",
            3: "1",
            4: "1",
            5: "8131",
            6: "3",
            7: "1601609668",
            8: '\\"Black Mageweave Headband\\"',
            9: "nil",
            10: "1",
            11: "2",
            12: "false",
            13: "41",
            14: "8131",
            15: "0",
            16: "12500",
            17: "0",
            18: "false",
            19: '\\"Dikiliker\\"',
            20: "0",
            21: '\\"\\"',
            22: "10024",
            23: "0",
            24: "0",
            25: "0",
            26: "0",
            27: "",
        },
        22966: {
            0: 'r\\"',
            1: "60",
            2: "9",
            3: "0",
            4: "nil",
            5: "170000",
            6: "3",
            7: "1601609666",
            8: '\\"Grimoire of Corruption VII\\"',
            9: "nil",
            10: "1",
            11: "3",
            12: "false",
            13: "60",
            14: "170000",
            15: "0",
            16: "210000",
            17: "0",
            18: "false",
            19: '\\"Biblical\\"',
            20: "0",
            21: '\\"\\"',
            22: "21283",
            23: "0",
            24: "0",
            25: "0",
            26: "0",
            27: "",
        },
        26199: {
            0: 'r\\"',
            1: "44",
            2: "2",
            3: "10",
            4: "17",
            5: "196294",
            6: "2",
            7: "1601609667",
            8: '\\"Spiritchaser Staff of Spirit\\"',
            9: "nil",
            10: "1",
            11: "2",
            12: "false",
            13: "39",
            14: "196294",
            15: "0",
            16: "218104",
            17: "0",
            18: "false",
            19: '\\"Enjoythedots\\"',
            20: "0",
            21: '\\"\\"',
            22: "1613",
            23: "412",
            24: "0",
            25: "0",
            26: "426022272",
            27: "",
        },
    }
    example_df = pd.DataFrame.from_dict(example, orient="index")
    sources.process_auctioneer_data(example_df)
