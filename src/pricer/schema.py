"""Schema enforcement for project."""
import pandera as pa
from pandera import Column, Index

item_skeleton_raw_schema = pa.DataFrameSchema(
    columns={
        "min_holding": Column(pa.Int, nullable=True),
        "max_holding": Column(pa.Int, nullable=True),
        "max_sell": Column(pa.Int, nullable=True),
        "Buy": Column(pa.Bool, nullable=True, coerce=True),
        "Sell": Column(pa.Bool, nullable=True, coerce=True),
        "made_from": Column(pa.Object, nullable=True),
        "make_pass": Column(pa.Int, nullable=True),
        "vendor_price": Column(pa.Int, nullable=True),
    },
    strict=True,
    index=Index(pa.String),
)

item_skeleton_schema = pa.DataFrameSchema(
    columns={
        "min_holding": Column(pa.Int),
        "max_holding": Column(pa.Int),
        "max_sell": Column(pa.Int, nullable=True),
        "Buy": Column(pa.Int),
        "Sell": Column(pa.Int),
        "made_from": Column(pa.Bool),
        "make_pass": Column(pa.Int),
        "vendor_price": Column(pa.Int),
        "std_holding": Column(pa.Float),
        "mean_holding": Column(pa.Int),
    },
    strict=True,
    index=Index(pa.String),
)

auc_listings_raw_schema = pa.DataFrameSchema(
    columns={
        0: Column(pa.String),
        1: Column(pa.String),
        2: Column(pa.String),
        3: Column(pa.String),
        4: Column(pa.String),
        5: Column(pa.String),
        6: Column(pa.String),
        7: Column(pa.String),
        8: Column(pa.String),
        9: Column(pa.String),
        10: Column(pa.String),
        11: Column(pa.String),
        12: Column(pa.String),
        13: Column(pa.String),
        14: Column(pa.String),
        15: Column(pa.String),
        16: Column(pa.String),
        17: Column(pa.String),
        18: Column(pa.String),
        19: Column(pa.String),
        20: Column(pa.String),
        21: Column(pa.String),
        22: Column(pa.String),
        23: Column(pa.String),
        24: Column(pa.String),
        25: Column(pa.String),
        26: Column(pa.String),
        27: Column(pa.String),
    }
)

auc_listings_schema = pa.DataFrameSchema(
    columns={
        "item": Column(pa.String),
        "quantity": Column(pa.Int),
        "buy": Column(pa.Int),
        "sellername": Column(pa.String),
        "price_per": Column(pa.Int),
        "time_remaining": Column(pa.Int),
    }
)
