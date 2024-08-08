from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    transactions: _ClassVar[BlockField]
    missed: _ClassVar[BlockField]
    block_reward: _ClassVar[BlockField]
    size: _ClassVar[BlockField]
    proposer: _ClassVar[BlockField]
    validators: _ClassVar[BlockField]
    evidence: _ClassVar[BlockField]

class SwapFrom(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    optimal: _ClassVar[SwapFrom]
    bancor: _ClassVar[SwapFrom]
    pool: _ClassVar[SwapFrom]
transactions: BlockField
missed: BlockField
block_reward: BlockField
size: BlockField
proposer: BlockField
validators: BlockField
evidence: BlockField
optimal: SwapFrom
bancor: SwapFrom
pool: SwapFrom

class Coin(_message.Message):
    __slots__ = ("id", "symbol")
    ID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    id: int
    symbol: str
    def __init__(self, id: _Optional[int] = ..., symbol: _Optional[str] = ...) -> None: ...

class BestTradeRequest(_message.Message):
    __slots__ = ("sell_coin", "buy_coin", "amount", "type", "height", "max_depth")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        input: _ClassVar[BestTradeRequest.Type]
        output: _ClassVar[BestTradeRequest.Type]
    input: BestTradeRequest.Type
    output: BestTradeRequest.Type
    SELL_COIN_FIELD_NUMBER: _ClassVar[int]
    BUY_COIN_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    sell_coin: int
    buy_coin: int
    amount: str
    type: BestTradeRequest.Type
    height: int
    max_depth: int
    def __init__(self, sell_coin: _Optional[int] = ..., buy_coin: _Optional[int] = ..., amount: _Optional[str] = ..., type: _Optional[_Union[BestTradeRequest.Type, str]] = ..., height: _Optional[int] = ..., max_depth: _Optional[int] = ...) -> None: ...

class BestTradeResponse(_message.Message):
    __slots__ = ("path", "result")
    PATH_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedScalarFieldContainer[int]
    result: str
    def __init__(self, path: _Optional[_Iterable[int]] = ..., result: _Optional[str] = ...) -> None: ...

class BlocksRequest(_message.Message):
    __slots__ = ("from_height", "to_height", "fields", "failed_txs", "events")
    FROM_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TO_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_TXS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    from_height: int
    to_height: int
    fields: _containers.RepeatedScalarFieldContainer[BlockField]
    failed_txs: bool
    events: bool
    def __init__(self, from_height: _Optional[int] = ..., to_height: _Optional[int] = ..., fields: _Optional[_Iterable[_Union[BlockField, str]]] = ..., failed_txs: bool = ..., events: bool = ...) -> None: ...

class BlocksResponse(_message.Message):
    __slots__ = ("blocks",)
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[BlockResponse]
    def __init__(self, blocks: _Optional[_Iterable[_Union[BlockResponse, _Mapping]]] = ...) -> None: ...

class CommissionVotesRequest(_message.Message):
    __slots__ = ("target_version", "height")
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    target_version: int
    height: int
    def __init__(self, target_version: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class CommissionVotesResponse(_message.Message):
    __slots__ = ("votes",)
    class Vote(_message.Message):
        __slots__ = ("price", "public_keys")
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
        price: PriceCommissionResponse
        public_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, price: _Optional[_Union[PriceCommissionResponse, _Mapping]] = ..., public_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    VOTES_FIELD_NUMBER: _ClassVar[int]
    votes: _containers.RepeatedCompositeFieldContainer[CommissionVotesResponse.Vote]
    def __init__(self, votes: _Optional[_Iterable[_Union[CommissionVotesResponse.Vote, _Mapping]]] = ...) -> None: ...

class LimitOrderRequest(_message.Message):
    __slots__ = ("order_id", "height")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    height: int
    def __init__(self, order_id: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class LimitOrderResponse(_message.Message):
    __slots__ = ("id", "coin_sell", "coin_buy", "want_sell", "want_buy", "price", "owner", "height")
    ID_FIELD_NUMBER: _ClassVar[int]
    COIN_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_BUY_FIELD_NUMBER: _ClassVar[int]
    WANT_SELL_FIELD_NUMBER: _ClassVar[int]
    WANT_BUY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    id: int
    coin_sell: Coin
    coin_buy: Coin
    want_sell: str
    want_buy: str
    price: str
    owner: str
    height: int
    def __init__(self, id: _Optional[int] = ..., coin_sell: _Optional[_Union[Coin, _Mapping]] = ..., coin_buy: _Optional[_Union[Coin, _Mapping]] = ..., want_sell: _Optional[str] = ..., want_buy: _Optional[str] = ..., price: _Optional[str] = ..., owner: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class LimitOrdersOfPoolRequest(_message.Message):
    __slots__ = ("sell_coin", "buy_coin", "limit", "height")
    SELL_COIN_FIELD_NUMBER: _ClassVar[int]
    BUY_COIN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    sell_coin: int
    buy_coin: int
    limit: int
    height: int
    def __init__(self, sell_coin: _Optional[int] = ..., buy_coin: _Optional[int] = ..., limit: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class LimitOrdersOfPoolResponse(_message.Message):
    __slots__ = ("pool_price", "orders")
    POOL_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    pool_price: str
    orders: _containers.RepeatedCompositeFieldContainer[LimitOrderResponse]
    def __init__(self, pool_price: _Optional[str] = ..., orders: _Optional[_Iterable[_Union[LimitOrderResponse, _Mapping]]] = ...) -> None: ...

class LimitOrdersRequest(_message.Message):
    __slots__ = ("ids", "height")
    IDS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    height: int
    def __init__(self, ids: _Optional[_Iterable[int]] = ..., height: _Optional[int] = ...) -> None: ...

class LimitOrdersResponse(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[LimitOrderResponse]
    def __init__(self, orders: _Optional[_Iterable[_Union[LimitOrderResponse, _Mapping]]] = ...) -> None: ...

class UpdateVotesRequest(_message.Message):
    __slots__ = ("target_version", "height")
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    target_version: int
    height: int
    def __init__(self, target_version: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class UpdateVotesResponse(_message.Message):
    __slots__ = ("votes",)
    class Vote(_message.Message):
        __slots__ = ("version", "public_keys")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
        version: str
        public_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, version: _Optional[str] = ..., public_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    VOTES_FIELD_NUMBER: _ClassVar[int]
    votes: _containers.RepeatedCompositeFieldContainer[UpdateVotesResponse.Vote]
    def __init__(self, votes: _Optional[_Iterable[_Union[UpdateVotesResponse.Vote, _Mapping]]] = ...) -> None: ...

class VersionNetworkRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VersionNetworkResponse(_message.Message):
    __slots__ = ("current", "versions")
    class Version(_message.Message):
        __slots__ = ("name", "height")
        NAME_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        name: str
        height: int
        def __init__(self, name: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    current: str
    versions: _containers.RepeatedCompositeFieldContainer[VersionNetworkResponse.Version]
    def __init__(self, current: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[VersionNetworkResponse.Version, _Mapping]]] = ...) -> None: ...

class PriceCommissionRequest(_message.Message):
    __slots__ = ("height",)
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class PriceCommissionResponse(_message.Message):
    __slots__ = ("coin", "payload_byte", "send", "buy_bancor", "sell_bancor", "sell_all_bancor", "buy_pool_base", "buy_pool_delta", "sell_pool_base", "sell_pool_delta", "sell_all_pool_base", "sell_all_pool_delta", "create_ticker3", "create_ticker4", "create_ticker5", "create_ticker6", "create_ticker7_10", "create_coin", "create_token", "recreate_coin", "recreate_token", "declare_candidacy", "delegate", "unbond", "redeem_check", "set_candidate_on", "set_candidate_off", "create_multisig", "multisend_base", "multisend_delta", "edit_candidate", "set_halt_block", "edit_ticker_owner", "edit_multisig", "edit_candidate_public_key", "create_swap_pool", "add_liquidity", "remove_liquidity", "edit_candidate_commission", "mint_token", "burn_token", "vote_commission", "vote_update", "failed_tx", "add_limit_order", "remove_limit_order", "move_stake", "lock_stake", "lock")
    COIN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_BYTE_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    BUY_BANCOR_FIELD_NUMBER: _ClassVar[int]
    SELL_BANCOR_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_BANCOR_FIELD_NUMBER: _ClassVar[int]
    BUY_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    BUY_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    SELL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    SELL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER3_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER4_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER5_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER6_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER7_10_FIELD_NUMBER: _ClassVar[int]
    CREATE_COIN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECREATE_COIN_FIELD_NUMBER: _ClassVar[int]
    RECREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DECLARE_CANDIDACY_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_FIELD_NUMBER: _ClassVar[int]
    UNBOND_FIELD_NUMBER: _ClassVar[int]
    REDEEM_CHECK_FIELD_NUMBER: _ClassVar[int]
    SET_CANDIDATE_ON_FIELD_NUMBER: _ClassVar[int]
    SET_CANDIDATE_OFF_FIELD_NUMBER: _ClassVar[int]
    CREATE_MULTISIG_FIELD_NUMBER: _ClassVar[int]
    MULTISEND_BASE_FIELD_NUMBER: _ClassVar[int]
    MULTISEND_DELTA_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    SET_HALT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    EDIT_TICKER_OWNER_FIELD_NUMBER: _ClassVar[int]
    EDIT_MULTISIG_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_SWAP_POOL_FIELD_NUMBER: _ClassVar[int]
    ADD_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    MINT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BURN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VOTE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    VOTE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    FAILED_TX_FIELD_NUMBER: _ClassVar[int]
    ADD_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
    MOVE_STAKE_FIELD_NUMBER: _ClassVar[int]
    LOCK_STAKE_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    coin: Coin
    payload_byte: str
    send: str
    buy_bancor: str
    sell_bancor: str
    sell_all_bancor: str
    buy_pool_base: str
    buy_pool_delta: str
    sell_pool_base: str
    sell_pool_delta: str
    sell_all_pool_base: str
    sell_all_pool_delta: str
    create_ticker3: str
    create_ticker4: str
    create_ticker5: str
    create_ticker6: str
    create_ticker7_10: str
    create_coin: str
    create_token: str
    recreate_coin: str
    recreate_token: str
    declare_candidacy: str
    delegate: str
    unbond: str
    redeem_check: str
    set_candidate_on: str
    set_candidate_off: str
    create_multisig: str
    multisend_base: str
    multisend_delta: str
    edit_candidate: str
    set_halt_block: str
    edit_ticker_owner: str
    edit_multisig: str
    edit_candidate_public_key: str
    create_swap_pool: str
    add_liquidity: str
    remove_liquidity: str
    edit_candidate_commission: str
    mint_token: str
    burn_token: str
    vote_commission: str
    vote_update: str
    failed_tx: str
    add_limit_order: str
    remove_limit_order: str
    move_stake: str
    lock_stake: str
    lock: str
    def __init__(self, coin: _Optional[_Union[Coin, _Mapping]] = ..., payload_byte: _Optional[str] = ..., send: _Optional[str] = ..., buy_bancor: _Optional[str] = ..., sell_bancor: _Optional[str] = ..., sell_all_bancor: _Optional[str] = ..., buy_pool_base: _Optional[str] = ..., buy_pool_delta: _Optional[str] = ..., sell_pool_base: _Optional[str] = ..., sell_pool_delta: _Optional[str] = ..., sell_all_pool_base: _Optional[str] = ..., sell_all_pool_delta: _Optional[str] = ..., create_ticker3: _Optional[str] = ..., create_ticker4: _Optional[str] = ..., create_ticker5: _Optional[str] = ..., create_ticker6: _Optional[str] = ..., create_ticker7_10: _Optional[str] = ..., create_coin: _Optional[str] = ..., create_token: _Optional[str] = ..., recreate_coin: _Optional[str] = ..., recreate_token: _Optional[str] = ..., declare_candidacy: _Optional[str] = ..., delegate: _Optional[str] = ..., unbond: _Optional[str] = ..., redeem_check: _Optional[str] = ..., set_candidate_on: _Optional[str] = ..., set_candidate_off: _Optional[str] = ..., create_multisig: _Optional[str] = ..., multisend_base: _Optional[str] = ..., multisend_delta: _Optional[str] = ..., edit_candidate: _Optional[str] = ..., set_halt_block: _Optional[str] = ..., edit_ticker_owner: _Optional[str] = ..., edit_multisig: _Optional[str] = ..., edit_candidate_public_key: _Optional[str] = ..., create_swap_pool: _Optional[str] = ..., add_liquidity: _Optional[str] = ..., remove_liquidity: _Optional[str] = ..., edit_candidate_commission: _Optional[str] = ..., mint_token: _Optional[str] = ..., burn_token: _Optional[str] = ..., vote_commission: _Optional[str] = ..., vote_update: _Optional[str] = ..., failed_tx: _Optional[str] = ..., add_limit_order: _Optional[str] = ..., remove_limit_order: _Optional[str] = ..., move_stake: _Optional[str] = ..., lock_stake: _Optional[str] = ..., lock: _Optional[str] = ...) -> None: ...

class SwapPoolsRequest(_message.Message):
    __slots__ = ("height", "orders")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    height: int
    orders: bool
    def __init__(self, height: _Optional[int] = ..., orders: bool = ...) -> None: ...

class SwapPoolsResponse(_message.Message):
    __slots__ = ("pools",)
    class SwapPool(_message.Message):
        __slots__ = ("id", "price", "coin0", "coin1", "amount0", "amount1", "liquidity", "orders_sell", "orders_buy")
        class LimitOrder(_message.Message):
            __slots__ = ("id", "want_sell", "want_buy", "price", "owner", "height")
            ID_FIELD_NUMBER: _ClassVar[int]
            WANT_SELL_FIELD_NUMBER: _ClassVar[int]
            WANT_BUY_FIELD_NUMBER: _ClassVar[int]
            PRICE_FIELD_NUMBER: _ClassVar[int]
            OWNER_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            id: int
            want_sell: str
            want_buy: str
            price: str
            owner: str
            height: int
            def __init__(self, id: _Optional[int] = ..., want_sell: _Optional[str] = ..., want_buy: _Optional[str] = ..., price: _Optional[str] = ..., owner: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        COIN0_FIELD_NUMBER: _ClassVar[int]
        COIN1_FIELD_NUMBER: _ClassVar[int]
        AMOUNT0_FIELD_NUMBER: _ClassVar[int]
        AMOUNT1_FIELD_NUMBER: _ClassVar[int]
        LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
        ORDERS_SELL_FIELD_NUMBER: _ClassVar[int]
        ORDERS_BUY_FIELD_NUMBER: _ClassVar[int]
        id: int
        price: str
        coin0: int
        coin1: int
        amount0: str
        amount1: str
        liquidity: str
        orders_sell: _containers.RepeatedCompositeFieldContainer[SwapPoolsResponse.SwapPool.LimitOrder]
        orders_buy: _containers.RepeatedCompositeFieldContainer[SwapPoolsResponse.SwapPool.LimitOrder]
        def __init__(self, id: _Optional[int] = ..., price: _Optional[str] = ..., coin0: _Optional[int] = ..., coin1: _Optional[int] = ..., amount0: _Optional[str] = ..., amount1: _Optional[str] = ..., liquidity: _Optional[str] = ..., orders_sell: _Optional[_Iterable[_Union[SwapPoolsResponse.SwapPool.LimitOrder, _Mapping]]] = ..., orders_buy: _Optional[_Iterable[_Union[SwapPoolsResponse.SwapPool.LimitOrder, _Mapping]]] = ...) -> None: ...
    POOLS_FIELD_NUMBER: _ClassVar[int]
    pools: _containers.RepeatedCompositeFieldContainer[SwapPoolsResponse.SwapPool]
    def __init__(self, pools: _Optional[_Iterable[_Union[SwapPoolsResponse.SwapPool, _Mapping]]] = ...) -> None: ...

class SwapPoolRequest(_message.Message):
    __slots__ = ("coin0", "coin1", "height")
    COIN0_FIELD_NUMBER: _ClassVar[int]
    COIN1_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    coin0: int
    coin1: int
    height: int
    def __init__(self, coin0: _Optional[int] = ..., coin1: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class SwapPoolResponse(_message.Message):
    __slots__ = ("id", "price", "amount0", "amount1", "liquidity")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT0_FIELD_NUMBER: _ClassVar[int]
    AMOUNT1_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    id: int
    price: str
    amount0: str
    amount1: str
    liquidity: str
    def __init__(self, id: _Optional[int] = ..., price: _Optional[str] = ..., amount0: _Optional[str] = ..., amount1: _Optional[str] = ..., liquidity: _Optional[str] = ...) -> None: ...

class SwapPoolProviderRequest(_message.Message):
    __slots__ = ("coin0", "coin1", "provider", "height")
    COIN0_FIELD_NUMBER: _ClassVar[int]
    COIN1_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    coin0: int
    coin1: int
    provider: str
    height: int
    def __init__(self, coin0: _Optional[int] = ..., coin1: _Optional[int] = ..., provider: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("protocol_version", "id", "listen_addr", "network", "version", "channels", "moniker", "other")
    class ProtocolVersion(_message.Message):
        __slots__ = ("p2p", "block", "app")
        P2P_FIELD_NUMBER: _ClassVar[int]
        BLOCK_FIELD_NUMBER: _ClassVar[int]
        APP_FIELD_NUMBER: _ClassVar[int]
        p2p: int
        block: int
        app: int
        def __init__(self, p2p: _Optional[int] = ..., block: _Optional[int] = ..., app: _Optional[int] = ...) -> None: ...
    class Other(_message.Message):
        __slots__ = ("tx_index", "rpc_address")
        TX_INDEX_FIELD_NUMBER: _ClassVar[int]
        RPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        tx_index: str
        rpc_address: str
        def __init__(self, tx_index: _Optional[str] = ..., rpc_address: _Optional[str] = ...) -> None: ...
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LISTEN_ADDR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MONIKER_FIELD_NUMBER: _ClassVar[int]
    OTHER_FIELD_NUMBER: _ClassVar[int]
    protocol_version: NodeInfo.ProtocolVersion
    id: str
    listen_addr: str
    network: str
    version: str
    channels: str
    moniker: str
    other: NodeInfo.Other
    def __init__(self, protocol_version: _Optional[_Union[NodeInfo.ProtocolVersion, _Mapping]] = ..., id: _Optional[str] = ..., listen_addr: _Optional[str] = ..., network: _Optional[str] = ..., version: _Optional[str] = ..., channels: _Optional[str] = ..., moniker: _Optional[str] = ..., other: _Optional[_Union[NodeInfo.Other, _Mapping]] = ...) -> None: ...

class NetInfoResponse(_message.Message):
    __slots__ = ("listening", "listeners", "count_peers", "peers")
    class Peer(_message.Message):
        __slots__ = ("latest_block_height", "node_info", "is_outbound", "connection_status", "remote_ip")
        class ConnectionStatus(_message.Message):
            __slots__ = ("duration", "SendMonitor", "RecvMonitor", "channels")
            class Monitor(_message.Message):
                __slots__ = ("active", "start", "duration", "idle", "bytes", "samples", "inst_rate", "cur_rate", "avg_rate", "peak_rate", "bytes_rem", "time_rem", "progress")
                ACTIVE_FIELD_NUMBER: _ClassVar[int]
                START_FIELD_NUMBER: _ClassVar[int]
                DURATION_FIELD_NUMBER: _ClassVar[int]
                IDLE_FIELD_NUMBER: _ClassVar[int]
                BYTES_FIELD_NUMBER: _ClassVar[int]
                SAMPLES_FIELD_NUMBER: _ClassVar[int]
                INST_RATE_FIELD_NUMBER: _ClassVar[int]
                CUR_RATE_FIELD_NUMBER: _ClassVar[int]
                AVG_RATE_FIELD_NUMBER: _ClassVar[int]
                PEAK_RATE_FIELD_NUMBER: _ClassVar[int]
                BYTES_REM_FIELD_NUMBER: _ClassVar[int]
                TIME_REM_FIELD_NUMBER: _ClassVar[int]
                PROGRESS_FIELD_NUMBER: _ClassVar[int]
                active: bool
                start: str
                duration: int
                idle: int
                bytes: int
                samples: int
                inst_rate: int
                cur_rate: int
                avg_rate: int
                peak_rate: int
                bytes_rem: int
                time_rem: int
                progress: int
                def __init__(self, active: bool = ..., start: _Optional[str] = ..., duration: _Optional[int] = ..., idle: _Optional[int] = ..., bytes: _Optional[int] = ..., samples: _Optional[int] = ..., inst_rate: _Optional[int] = ..., cur_rate: _Optional[int] = ..., avg_rate: _Optional[int] = ..., peak_rate: _Optional[int] = ..., bytes_rem: _Optional[int] = ..., time_rem: _Optional[int] = ..., progress: _Optional[int] = ...) -> None: ...
            class Channel(_message.Message):
                __slots__ = ("id", "send_queue_capacity", "send_queue_size", "priority", "recently_sent")
                ID_FIELD_NUMBER: _ClassVar[int]
                SEND_QUEUE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
                SEND_QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
                PRIORITY_FIELD_NUMBER: _ClassVar[int]
                RECENTLY_SENT_FIELD_NUMBER: _ClassVar[int]
                id: int
                send_queue_capacity: int
                send_queue_size: int
                priority: int
                recently_sent: int
                def __init__(self, id: _Optional[int] = ..., send_queue_capacity: _Optional[int] = ..., send_queue_size: _Optional[int] = ..., priority: _Optional[int] = ..., recently_sent: _Optional[int] = ...) -> None: ...
            DURATION_FIELD_NUMBER: _ClassVar[int]
            SENDMONITOR_FIELD_NUMBER: _ClassVar[int]
            RECVMONITOR_FIELD_NUMBER: _ClassVar[int]
            CHANNELS_FIELD_NUMBER: _ClassVar[int]
            duration: int
            SendMonitor: NetInfoResponse.Peer.ConnectionStatus.Monitor
            RecvMonitor: NetInfoResponse.Peer.ConnectionStatus.Monitor
            channels: _containers.RepeatedCompositeFieldContainer[NetInfoResponse.Peer.ConnectionStatus.Channel]
            def __init__(self, duration: _Optional[int] = ..., SendMonitor: _Optional[_Union[NetInfoResponse.Peer.ConnectionStatus.Monitor, _Mapping]] = ..., RecvMonitor: _Optional[_Union[NetInfoResponse.Peer.ConnectionStatus.Monitor, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[NetInfoResponse.Peer.ConnectionStatus.Channel, _Mapping]]] = ...) -> None: ...
        LATEST_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        NODE_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        REMOTE_IP_FIELD_NUMBER: _ClassVar[int]
        latest_block_height: _wrappers_pb2.UInt64Value
        node_info: NodeInfo
        is_outbound: bool
        connection_status: NetInfoResponse.Peer.ConnectionStatus
        remote_ip: str
        def __init__(self, latest_block_height: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., node_info: _Optional[_Union[NodeInfo, _Mapping]] = ..., is_outbound: bool = ..., connection_status: _Optional[_Union[NetInfoResponse.Peer.ConnectionStatus, _Mapping]] = ..., remote_ip: _Optional[str] = ...) -> None: ...
    LISTENING_FIELD_NUMBER: _ClassVar[int]
    LISTENERS_FIELD_NUMBER: _ClassVar[int]
    COUNT_PEERS_FIELD_NUMBER: _ClassVar[int]
    PEERS_FIELD_NUMBER: _ClassVar[int]
    listening: bool
    listeners: _containers.RepeatedScalarFieldContainer[str]
    count_peers: int
    peers: _containers.RepeatedCompositeFieldContainer[NetInfoResponse.Peer]
    def __init__(self, listening: bool = ..., listeners: _Optional[_Iterable[str]] = ..., count_peers: _Optional[int] = ..., peers: _Optional[_Iterable[_Union[NetInfoResponse.Peer, _Mapping]]] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("version", "network", "initial_height", "latest_block_hash", "latest_app_hash", "latest_block_height", "latest_block_time", "keep_last_states", "total_slashed", "current_emission", "catching_up", "public_key", "node_id", "moniker")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    INITIAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LATEST_BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    LATEST_APP_HASH_FIELD_NUMBER: _ClassVar[int]
    LATEST_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LATEST_BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    KEEP_LAST_STATES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SLASHED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_EMISSION_FIELD_NUMBER: _ClassVar[int]
    CATCHING_UP_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MONIKER_FIELD_NUMBER: _ClassVar[int]
    version: str
    network: str
    initial_height: int
    latest_block_hash: str
    latest_app_hash: str
    latest_block_height: int
    latest_block_time: str
    keep_last_states: int
    total_slashed: str
    current_emission: str
    catching_up: bool
    public_key: str
    node_id: str
    moniker: str
    def __init__(self, version: _Optional[str] = ..., network: _Optional[str] = ..., initial_height: _Optional[int] = ..., latest_block_hash: _Optional[str] = ..., latest_app_hash: _Optional[str] = ..., latest_block_height: _Optional[int] = ..., latest_block_time: _Optional[str] = ..., keep_last_states: _Optional[int] = ..., total_slashed: _Optional[str] = ..., current_emission: _Optional[str] = ..., catching_up: bool = ..., public_key: _Optional[str] = ..., node_id: _Optional[str] = ..., moniker: _Optional[str] = ...) -> None: ...

class GenesisResponse(_message.Message):
    __slots__ = ("genesis_time", "chain_id", "initial_height", "consensus_params", "app_hash", "app_state")
    class ConsensusParams(_message.Message):
        __slots__ = ("block", "evidence", "validator", "version")
        class Block(_message.Message):
            __slots__ = ("max_bytes", "max_gas", "time_iota_ms")
            MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
            MAX_GAS_FIELD_NUMBER: _ClassVar[int]
            TIME_IOTA_MS_FIELD_NUMBER: _ClassVar[int]
            max_bytes: int
            max_gas: int
            time_iota_ms: int
            def __init__(self, max_bytes: _Optional[int] = ..., max_gas: _Optional[int] = ..., time_iota_ms: _Optional[int] = ...) -> None: ...
        class Evidence(_message.Message):
            __slots__ = ("max_age_num_blocks", "max_age_duration")
            MAX_AGE_NUM_BLOCKS_FIELD_NUMBER: _ClassVar[int]
            MAX_AGE_DURATION_FIELD_NUMBER: _ClassVar[int]
            max_age_num_blocks: int
            max_age_duration: int
            def __init__(self, max_age_num_blocks: _Optional[int] = ..., max_age_duration: _Optional[int] = ...) -> None: ...
        class Validator(_message.Message):
            __slots__ = ("pub_key_types",)
            PUB_KEY_TYPES_FIELD_NUMBER: _ClassVar[int]
            pub_key_types: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, pub_key_types: _Optional[_Iterable[str]] = ...) -> None: ...
        class Version(_message.Message):
            __slots__ = ("app_version",)
            APP_VERSION_FIELD_NUMBER: _ClassVar[int]
            app_version: int
            def __init__(self, app_version: _Optional[int] = ...) -> None: ...
        BLOCK_FIELD_NUMBER: _ClassVar[int]
        EVIDENCE_FIELD_NUMBER: _ClassVar[int]
        VALIDATOR_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        block: GenesisResponse.ConsensusParams.Block
        evidence: GenesisResponse.ConsensusParams.Evidence
        validator: GenesisResponse.ConsensusParams.Validator
        version: GenesisResponse.ConsensusParams.Version
        def __init__(self, block: _Optional[_Union[GenesisResponse.ConsensusParams.Block, _Mapping]] = ..., evidence: _Optional[_Union[GenesisResponse.ConsensusParams.Evidence, _Mapping]] = ..., validator: _Optional[_Union[GenesisResponse.ConsensusParams.Validator, _Mapping]] = ..., version: _Optional[_Union[GenesisResponse.ConsensusParams.Version, _Mapping]] = ...) -> None: ...
    class AppState(_message.Message):
        __slots__ = ("version", "note", "validators", "candidates", "deleted_candidates", "coins", "frozen_funds", "block_list_candidates", "waitlist", "accounts", "halt_blocks", "pools", "next_order_id", "commission", "commission_votes", "update_votes", "used_checks", "max_gas", "total_slashed", "versions", "emission", "prev_reward")
        class Validators(_message.Message):
            __slots__ = ("total_bip_stake", "public_key", "accum_reward", "absent_times")
            TOTAL_BIP_STAKE_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
            ACCUM_REWARD_FIELD_NUMBER: _ClassVar[int]
            ABSENT_TIMES_FIELD_NUMBER: _ClassVar[int]
            total_bip_stake: str
            public_key: str
            accum_reward: str
            absent_times: str
            def __init__(self, total_bip_stake: _Optional[str] = ..., public_key: _Optional[str] = ..., accum_reward: _Optional[str] = ..., absent_times: _Optional[str] = ...) -> None: ...
        class Candidate(_message.Message):
            __slots__ = ("id", "reward_address", "owner_address", "control_address", "total_bip_stake", "public_key", "commission", "stakes", "updates", "status", "jailed_until", "last_edit_commission_height")
            class Stake(_message.Message):
                __slots__ = ("owner", "coin", "value", "bip_value")
                OWNER_FIELD_NUMBER: _ClassVar[int]
                COIN_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
                owner: str
                coin: int
                value: str
                bip_value: str
                def __init__(self, owner: _Optional[str] = ..., coin: _Optional[int] = ..., value: _Optional[str] = ..., bip_value: _Optional[str] = ...) -> None: ...
            ID_FIELD_NUMBER: _ClassVar[int]
            REWARD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            CONTROL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            TOTAL_BIP_STAKE_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
            COMMISSION_FIELD_NUMBER: _ClassVar[int]
            STAKES_FIELD_NUMBER: _ClassVar[int]
            UPDATES_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            JAILED_UNTIL_FIELD_NUMBER: _ClassVar[int]
            LAST_EDIT_COMMISSION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
            id: int
            reward_address: str
            owner_address: str
            control_address: str
            total_bip_stake: str
            public_key: str
            commission: int
            stakes: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Candidate.Stake]
            updates: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Candidate.Stake]
            status: int
            jailed_until: int
            last_edit_commission_height: int
            def __init__(self, id: _Optional[int] = ..., reward_address: _Optional[str] = ..., owner_address: _Optional[str] = ..., control_address: _Optional[str] = ..., total_bip_stake: _Optional[str] = ..., public_key: _Optional[str] = ..., commission: _Optional[int] = ..., stakes: _Optional[_Iterable[_Union[GenesisResponse.AppState.Candidate.Stake, _Mapping]]] = ..., updates: _Optional[_Iterable[_Union[GenesisResponse.AppState.Candidate.Stake, _Mapping]]] = ..., status: _Optional[int] = ..., jailed_until: _Optional[int] = ..., last_edit_commission_height: _Optional[int] = ...) -> None: ...
        class DeletedCandidate(_message.Message):
            __slots__ = ("id", "public_key")
            ID_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
            id: int
            public_key: str
            def __init__(self, id: _Optional[int] = ..., public_key: _Optional[str] = ...) -> None: ...
        class Coin(_message.Message):
            __slots__ = ("id", "name", "symbol", "volume", "crr", "reserve", "max_supply", "version", "owner_address", "mintable", "burnable")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            SYMBOL_FIELD_NUMBER: _ClassVar[int]
            VOLUME_FIELD_NUMBER: _ClassVar[int]
            CRR_FIELD_NUMBER: _ClassVar[int]
            RESERVE_FIELD_NUMBER: _ClassVar[int]
            MAX_SUPPLY_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            MINTABLE_FIELD_NUMBER: _ClassVar[int]
            BURNABLE_FIELD_NUMBER: _ClassVar[int]
            id: int
            name: str
            symbol: str
            volume: str
            crr: int
            reserve: str
            max_supply: str
            version: int
            owner_address: _wrappers_pb2.StringValue
            mintable: bool
            burnable: bool
            def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., volume: _Optional[str] = ..., crr: _Optional[int] = ..., reserve: _Optional[str] = ..., max_supply: _Optional[str] = ..., version: _Optional[int] = ..., owner_address: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mintable: bool = ..., burnable: bool = ...) -> None: ...
        class FrozenFund(_message.Message):
            __slots__ = ("height", "address", "candidate_key", "candidate_id", "coin", "value", "to_candidate_key")
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
            CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
            COIN_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            TO_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
            height: int
            address: str
            candidate_key: _wrappers_pb2.StringValue
            candidate_id: int
            coin: int
            value: str
            to_candidate_key: _wrappers_pb2.StringValue
            def __init__(self, height: _Optional[int] = ..., address: _Optional[str] = ..., candidate_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., candidate_id: _Optional[int] = ..., coin: _Optional[int] = ..., value: _Optional[str] = ..., to_candidate_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        class Waitlist(_message.Message):
            __slots__ = ("candidate_id", "owner", "coin", "value")
            CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
            OWNER_FIELD_NUMBER: _ClassVar[int]
            COIN_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            candidate_id: int
            owner: str
            coin: int
            value: str
            def __init__(self, candidate_id: _Optional[int] = ..., owner: _Optional[str] = ..., coin: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
        class Account(_message.Message):
            __slots__ = ("address", "balance", "nonce", "multisig_data", "lock_stake_until_block")
            class Balance(_message.Message):
                __slots__ = ("coin", "value")
                COIN_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                coin: int
                value: str
                def __init__(self, coin: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
            class MultisigData(_message.Message):
                __slots__ = ("threshold", "weights", "addresses")
                THRESHOLD_FIELD_NUMBER: _ClassVar[int]
                WEIGHTS_FIELD_NUMBER: _ClassVar[int]
                ADDRESSES_FIELD_NUMBER: _ClassVar[int]
                threshold: int
                weights: _containers.RepeatedScalarFieldContainer[int]
                addresses: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, threshold: _Optional[int] = ..., weights: _Optional[_Iterable[int]] = ..., addresses: _Optional[_Iterable[str]] = ...) -> None: ...
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            BALANCE_FIELD_NUMBER: _ClassVar[int]
            NONCE_FIELD_NUMBER: _ClassVar[int]
            MULTISIG_DATA_FIELD_NUMBER: _ClassVar[int]
            LOCK_STAKE_UNTIL_BLOCK_FIELD_NUMBER: _ClassVar[int]
            address: str
            balance: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Account.Balance]
            nonce: int
            multisig_data: GenesisResponse.AppState.Account.MultisigData
            lock_stake_until_block: int
            def __init__(self, address: _Optional[str] = ..., balance: _Optional[_Iterable[_Union[GenesisResponse.AppState.Account.Balance, _Mapping]]] = ..., nonce: _Optional[int] = ..., multisig_data: _Optional[_Union[GenesisResponse.AppState.Account.MultisigData, _Mapping]] = ..., lock_stake_until_block: _Optional[int] = ...) -> None: ...
        class HaltBlock(_message.Message):
            __slots__ = ("height", "candidate_key")
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
            height: int
            candidate_key: str
            def __init__(self, height: _Optional[int] = ..., candidate_key: _Optional[str] = ...) -> None: ...
        class Pool(_message.Message):
            __slots__ = ("coin0", "coin1", "reserve0", "reserve1", "id", "orders")
            class Order(_message.Message):
                __slots__ = ("is_sale", "volume0", "volume1", "id", "owner", "height")
                IS_SALE_FIELD_NUMBER: _ClassVar[int]
                VOLUME0_FIELD_NUMBER: _ClassVar[int]
                VOLUME1_FIELD_NUMBER: _ClassVar[int]
                ID_FIELD_NUMBER: _ClassVar[int]
                OWNER_FIELD_NUMBER: _ClassVar[int]
                HEIGHT_FIELD_NUMBER: _ClassVar[int]
                is_sale: bool
                volume0: str
                volume1: str
                id: int
                owner: str
                height: int
                def __init__(self, is_sale: bool = ..., volume0: _Optional[str] = ..., volume1: _Optional[str] = ..., id: _Optional[int] = ..., owner: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...
            COIN0_FIELD_NUMBER: _ClassVar[int]
            COIN1_FIELD_NUMBER: _ClassVar[int]
            RESERVE0_FIELD_NUMBER: _ClassVar[int]
            RESERVE1_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            ORDERS_FIELD_NUMBER: _ClassVar[int]
            coin0: int
            coin1: int
            reserve0: str
            reserve1: str
            id: int
            orders: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Pool.Order]
            def __init__(self, coin0: _Optional[int] = ..., coin1: _Optional[int] = ..., reserve0: _Optional[str] = ..., reserve1: _Optional[str] = ..., id: _Optional[int] = ..., orders: _Optional[_Iterable[_Union[GenesisResponse.AppState.Pool.Order, _Mapping]]] = ...) -> None: ...
        class Commission(_message.Message):
            __slots__ = ("coin", "payload_byte", "send", "buy_bancor", "sell_bancor", "sell_all_bancor", "buy_pool_base", "buy_pool_delta", "sell_pool_base", "sell_pool_delta", "sell_all_pool_base", "sell_all_pool_delta", "create_ticker3", "create_ticker4", "create_ticker5", "create_ticker6", "create_ticker7_10", "create_coin", "create_token", "recreate_coin", "recreate_token", "declare_candidacy", "delegate", "unbond", "redeem_check", "set_candidate_on", "set_candidate_off", "create_multisig", "multisend_base", "multisend_delta", "edit_candidate", "set_halt_block", "edit_ticker_owner", "edit_multisig", "edit_candidate_public_key", "create_swap_pool", "add_liquidity", "remove_liquidity", "edit_candidate_commission", "mint_token", "burn_token", "vote_commission", "vote_update", "failed_tx", "add_limit_order", "remove_limit_order", "move_stake", "lock_stake", "lock")
            COIN_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_BYTE_FIELD_NUMBER: _ClassVar[int]
            SEND_FIELD_NUMBER: _ClassVar[int]
            BUY_BANCOR_FIELD_NUMBER: _ClassVar[int]
            SELL_BANCOR_FIELD_NUMBER: _ClassVar[int]
            SELL_ALL_BANCOR_FIELD_NUMBER: _ClassVar[int]
            BUY_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
            BUY_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
            SELL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
            SELL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
            SELL_ALL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
            SELL_ALL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
            CREATE_TICKER3_FIELD_NUMBER: _ClassVar[int]
            CREATE_TICKER4_FIELD_NUMBER: _ClassVar[int]
            CREATE_TICKER5_FIELD_NUMBER: _ClassVar[int]
            CREATE_TICKER6_FIELD_NUMBER: _ClassVar[int]
            CREATE_TICKER7_10_FIELD_NUMBER: _ClassVar[int]
            CREATE_COIN_FIELD_NUMBER: _ClassVar[int]
            CREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
            RECREATE_COIN_FIELD_NUMBER: _ClassVar[int]
            RECREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
            DECLARE_CANDIDACY_FIELD_NUMBER: _ClassVar[int]
            DELEGATE_FIELD_NUMBER: _ClassVar[int]
            UNBOND_FIELD_NUMBER: _ClassVar[int]
            REDEEM_CHECK_FIELD_NUMBER: _ClassVar[int]
            SET_CANDIDATE_ON_FIELD_NUMBER: _ClassVar[int]
            SET_CANDIDATE_OFF_FIELD_NUMBER: _ClassVar[int]
            CREATE_MULTISIG_FIELD_NUMBER: _ClassVar[int]
            MULTISEND_BASE_FIELD_NUMBER: _ClassVar[int]
            MULTISEND_DELTA_FIELD_NUMBER: _ClassVar[int]
            EDIT_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            SET_HALT_BLOCK_FIELD_NUMBER: _ClassVar[int]
            EDIT_TICKER_OWNER_FIELD_NUMBER: _ClassVar[int]
            EDIT_MULTISIG_FIELD_NUMBER: _ClassVar[int]
            EDIT_CANDIDATE_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
            CREATE_SWAP_POOL_FIELD_NUMBER: _ClassVar[int]
            ADD_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
            REMOVE_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
            EDIT_CANDIDATE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
            MINT_TOKEN_FIELD_NUMBER: _ClassVar[int]
            BURN_TOKEN_FIELD_NUMBER: _ClassVar[int]
            VOTE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
            VOTE_UPDATE_FIELD_NUMBER: _ClassVar[int]
            FAILED_TX_FIELD_NUMBER: _ClassVar[int]
            ADD_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
            REMOVE_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
            MOVE_STAKE_FIELD_NUMBER: _ClassVar[int]
            LOCK_STAKE_FIELD_NUMBER: _ClassVar[int]
            LOCK_FIELD_NUMBER: _ClassVar[int]
            coin: int
            payload_byte: str
            send: str
            buy_bancor: str
            sell_bancor: str
            sell_all_bancor: str
            buy_pool_base: str
            buy_pool_delta: str
            sell_pool_base: str
            sell_pool_delta: str
            sell_all_pool_base: str
            sell_all_pool_delta: str
            create_ticker3: str
            create_ticker4: str
            create_ticker5: str
            create_ticker6: str
            create_ticker7_10: str
            create_coin: str
            create_token: str
            recreate_coin: str
            recreate_token: str
            declare_candidacy: str
            delegate: str
            unbond: str
            redeem_check: str
            set_candidate_on: str
            set_candidate_off: str
            create_multisig: str
            multisend_base: str
            multisend_delta: str
            edit_candidate: str
            set_halt_block: str
            edit_ticker_owner: str
            edit_multisig: str
            edit_candidate_public_key: str
            create_swap_pool: str
            add_liquidity: str
            remove_liquidity: str
            edit_candidate_commission: str
            mint_token: str
            burn_token: str
            vote_commission: str
            vote_update: str
            failed_tx: str
            add_limit_order: str
            remove_limit_order: str
            move_stake: str
            lock_stake: str
            lock: str
            def __init__(self, coin: _Optional[int] = ..., payload_byte: _Optional[str] = ..., send: _Optional[str] = ..., buy_bancor: _Optional[str] = ..., sell_bancor: _Optional[str] = ..., sell_all_bancor: _Optional[str] = ..., buy_pool_base: _Optional[str] = ..., buy_pool_delta: _Optional[str] = ..., sell_pool_base: _Optional[str] = ..., sell_pool_delta: _Optional[str] = ..., sell_all_pool_base: _Optional[str] = ..., sell_all_pool_delta: _Optional[str] = ..., create_ticker3: _Optional[str] = ..., create_ticker4: _Optional[str] = ..., create_ticker5: _Optional[str] = ..., create_ticker6: _Optional[str] = ..., create_ticker7_10: _Optional[str] = ..., create_coin: _Optional[str] = ..., create_token: _Optional[str] = ..., recreate_coin: _Optional[str] = ..., recreate_token: _Optional[str] = ..., declare_candidacy: _Optional[str] = ..., delegate: _Optional[str] = ..., unbond: _Optional[str] = ..., redeem_check: _Optional[str] = ..., set_candidate_on: _Optional[str] = ..., set_candidate_off: _Optional[str] = ..., create_multisig: _Optional[str] = ..., multisend_base: _Optional[str] = ..., multisend_delta: _Optional[str] = ..., edit_candidate: _Optional[str] = ..., set_halt_block: _Optional[str] = ..., edit_ticker_owner: _Optional[str] = ..., edit_multisig: _Optional[str] = ..., edit_candidate_public_key: _Optional[str] = ..., create_swap_pool: _Optional[str] = ..., add_liquidity: _Optional[str] = ..., remove_liquidity: _Optional[str] = ..., edit_candidate_commission: _Optional[str] = ..., mint_token: _Optional[str] = ..., burn_token: _Optional[str] = ..., vote_commission: _Optional[str] = ..., vote_update: _Optional[str] = ..., failed_tx: _Optional[str] = ..., add_limit_order: _Optional[str] = ..., remove_limit_order: _Optional[str] = ..., move_stake: _Optional[str] = ..., lock_stake: _Optional[str] = ..., lock: _Optional[str] = ...) -> None: ...
        class CommissionVote(_message.Message):
            __slots__ = ("height", "votes", "commission")
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            VOTES_FIELD_NUMBER: _ClassVar[int]
            COMMISSION_FIELD_NUMBER: _ClassVar[int]
            height: int
            votes: _containers.RepeatedScalarFieldContainer[str]
            commission: GenesisResponse.AppState.Commission
            def __init__(self, height: _Optional[int] = ..., votes: _Optional[_Iterable[str]] = ..., commission: _Optional[_Union[GenesisResponse.AppState.Commission, _Mapping]] = ...) -> None: ...
        class UpdateVote(_message.Message):
            __slots__ = ("height", "votes", "version")
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            VOTES_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            height: int
            votes: _containers.RepeatedScalarFieldContainer[str]
            version: str
            def __init__(self, height: _Optional[int] = ..., votes: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ...) -> None: ...
        class Version(_message.Message):
            __slots__ = ("height", "name")
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            height: int
            name: str
            def __init__(self, height: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
        class RewardPrice(_message.Message):
            __slots__ = ("time", "amount_bip", "amount_usdt", "off", "reward")
            TIME_FIELD_NUMBER: _ClassVar[int]
            AMOUNT_BIP_FIELD_NUMBER: _ClassVar[int]
            AMOUNT_USDT_FIELD_NUMBER: _ClassVar[int]
            OFF_FIELD_NUMBER: _ClassVar[int]
            REWARD_FIELD_NUMBER: _ClassVar[int]
            time: int
            amount_bip: str
            amount_usdt: str
            off: bool
            reward: str
            def __init__(self, time: _Optional[int] = ..., amount_bip: _Optional[str] = ..., amount_usdt: _Optional[str] = ..., off: bool = ..., reward: _Optional[str] = ...) -> None: ...
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NOTE_FIELD_NUMBER: _ClassVar[int]
        VALIDATORS_FIELD_NUMBER: _ClassVar[int]
        CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        DELETED_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        COINS_FIELD_NUMBER: _ClassVar[int]
        FROZEN_FUNDS_FIELD_NUMBER: _ClassVar[int]
        BLOCK_LIST_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        WAITLIST_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
        HALT_BLOCKS_FIELD_NUMBER: _ClassVar[int]
        POOLS_FIELD_NUMBER: _ClassVar[int]
        NEXT_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
        COMMISSION_FIELD_NUMBER: _ClassVar[int]
        COMMISSION_VOTES_FIELD_NUMBER: _ClassVar[int]
        UPDATE_VOTES_FIELD_NUMBER: _ClassVar[int]
        USED_CHECKS_FIELD_NUMBER: _ClassVar[int]
        MAX_GAS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SLASHED_FIELD_NUMBER: _ClassVar[int]
        VERSIONS_FIELD_NUMBER: _ClassVar[int]
        EMISSION_FIELD_NUMBER: _ClassVar[int]
        PREV_REWARD_FIELD_NUMBER: _ClassVar[int]
        version: str
        note: str
        validators: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Validators]
        candidates: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Candidate]
        deleted_candidates: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.DeletedCandidate]
        coins: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Coin]
        frozen_funds: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.FrozenFund]
        block_list_candidates: _containers.RepeatedScalarFieldContainer[str]
        waitlist: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Waitlist]
        accounts: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Account]
        halt_blocks: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.HaltBlock]
        pools: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Pool]
        next_order_id: int
        commission: GenesisResponse.AppState.Commission
        commission_votes: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.CommissionVote]
        update_votes: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.UpdateVote]
        used_checks: _containers.RepeatedScalarFieldContainer[str]
        max_gas: int
        total_slashed: str
        versions: _containers.RepeatedCompositeFieldContainer[GenesisResponse.AppState.Version]
        emission: str
        prev_reward: GenesisResponse.AppState.RewardPrice
        def __init__(self, version: _Optional[str] = ..., note: _Optional[str] = ..., validators: _Optional[_Iterable[_Union[GenesisResponse.AppState.Validators, _Mapping]]] = ..., candidates: _Optional[_Iterable[_Union[GenesisResponse.AppState.Candidate, _Mapping]]] = ..., deleted_candidates: _Optional[_Iterable[_Union[GenesisResponse.AppState.DeletedCandidate, _Mapping]]] = ..., coins: _Optional[_Iterable[_Union[GenesisResponse.AppState.Coin, _Mapping]]] = ..., frozen_funds: _Optional[_Iterable[_Union[GenesisResponse.AppState.FrozenFund, _Mapping]]] = ..., block_list_candidates: _Optional[_Iterable[str]] = ..., waitlist: _Optional[_Iterable[_Union[GenesisResponse.AppState.Waitlist, _Mapping]]] = ..., accounts: _Optional[_Iterable[_Union[GenesisResponse.AppState.Account, _Mapping]]] = ..., halt_blocks: _Optional[_Iterable[_Union[GenesisResponse.AppState.HaltBlock, _Mapping]]] = ..., pools: _Optional[_Iterable[_Union[GenesisResponse.AppState.Pool, _Mapping]]] = ..., next_order_id: _Optional[int] = ..., commission: _Optional[_Union[GenesisResponse.AppState.Commission, _Mapping]] = ..., commission_votes: _Optional[_Iterable[_Union[GenesisResponse.AppState.CommissionVote, _Mapping]]] = ..., update_votes: _Optional[_Iterable[_Union[GenesisResponse.AppState.UpdateVote, _Mapping]]] = ..., used_checks: _Optional[_Iterable[str]] = ..., max_gas: _Optional[int] = ..., total_slashed: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[GenesisResponse.AppState.Version, _Mapping]]] = ..., emission: _Optional[str] = ..., prev_reward: _Optional[_Union[GenesisResponse.AppState.RewardPrice, _Mapping]] = ...) -> None: ...
    GENESIS_TIME_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    APP_HASH_FIELD_NUMBER: _ClassVar[int]
    APP_STATE_FIELD_NUMBER: _ClassVar[int]
    genesis_time: str
    chain_id: str
    initial_height: int
    consensus_params: GenesisResponse.ConsensusParams
    app_hash: str
    app_state: GenesisResponse.AppState
    def __init__(self, genesis_time: _Optional[str] = ..., chain_id: _Optional[str] = ..., initial_height: _Optional[int] = ..., consensus_params: _Optional[_Union[GenesisResponse.ConsensusParams, _Mapping]] = ..., app_hash: _Optional[str] = ..., app_state: _Optional[_Union[GenesisResponse.AppState, _Mapping]] = ...) -> None: ...

class MinGasPriceResponse(_message.Message):
    __slots__ = ("min_gas_price",)
    MIN_GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    min_gas_price: int
    def __init__(self, min_gas_price: _Optional[int] = ...) -> None: ...

class BlockRequest(_message.Message):
    __slots__ = ("height", "fields", "failed_txs", "events")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_TXS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    height: int
    fields: _containers.RepeatedScalarFieldContainer[BlockField]
    failed_txs: bool
    events: bool
    def __init__(self, height: _Optional[int] = ..., fields: _Optional[_Iterable[_Union[BlockField, str]]] = ..., failed_txs: bool = ..., events: bool = ...) -> None: ...

class BlockResponse(_message.Message):
    __slots__ = ("hash", "height", "time", "transaction_count", "transactions", "block_reward", "locked_stake_rewards", "size", "proposer", "validators", "evidence", "missed", "events")
    class Validator(_message.Message):
        __slots__ = ("public_key", "signed")
        PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        SIGNED_FIELD_NUMBER: _ClassVar[int]
        public_key: str
        signed: bool
        def __init__(self, public_key: _Optional[str] = ..., signed: bool = ...) -> None: ...
    class Evidence(_message.Message):
        __slots__ = ("evidence",)
        EVIDENCE_FIELD_NUMBER: _ClassVar[int]
        evidence: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
        def __init__(self, evidence: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...
    HASH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REWARD_FIELD_NUMBER: _ClassVar[int]
    LOCKED_STAKE_REWARDS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    MISSED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    hash: str
    height: int
    time: str
    transaction_count: int
    transactions: _containers.RepeatedCompositeFieldContainer[TransactionResponse]
    block_reward: _wrappers_pb2.StringValue
    locked_stake_rewards: _wrappers_pb2.StringValue
    size: int
    proposer: str
    validators: _containers.RepeatedCompositeFieldContainer[BlockResponse.Validator]
    evidence: BlockResponse.Evidence
    missed: _containers.RepeatedScalarFieldContainer[str]
    events: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, hash: _Optional[str] = ..., height: _Optional[int] = ..., time: _Optional[str] = ..., transaction_count: _Optional[int] = ..., transactions: _Optional[_Iterable[_Union[TransactionResponse, _Mapping]]] = ..., block_reward: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., locked_stake_rewards: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., size: _Optional[int] = ..., proposer: _Optional[str] = ..., validators: _Optional[_Iterable[_Union[BlockResponse.Validator, _Mapping]]] = ..., evidence: _Optional[_Union[BlockResponse.Evidence, _Mapping]] = ..., missed: _Optional[_Iterable[str]] = ..., events: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class MaxGasPriceRequest(_message.Message):
    __slots__ = ("height",)
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class MaxGasPriceResponse(_message.Message):
    __slots__ = ("max_gas_price",)
    MAX_GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    max_gas_price: int
    def __init__(self, max_gas_price: _Optional[int] = ...) -> None: ...

class AddressRequest(_message.Message):
    __slots__ = ("address", "height", "delegated")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    address: str
    height: int
    delegated: bool
    def __init__(self, address: _Optional[str] = ..., height: _Optional[int] = ..., delegated: bool = ...) -> None: ...

class AddressBalance(_message.Message):
    __slots__ = ("coin", "value", "bip_value")
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
    coin: Coin
    value: str
    bip_value: str
    def __init__(self, coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ..., bip_value: _Optional[str] = ...) -> None: ...

class AddressDelegatedBalance(_message.Message):
    __slots__ = ("coin", "value", "bip_value", "delegate_bip_value")
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
    coin: Coin
    value: str
    bip_value: str
    delegate_bip_value: str
    def __init__(self, coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ..., bip_value: _Optional[str] = ..., delegate_bip_value: _Optional[str] = ...) -> None: ...

class AddressResponse(_message.Message):
    __slots__ = ("balance", "delegated", "total", "transaction_count", "bip_value", "locked_stake_until_block", "multisig")
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_STAKE_UNTIL_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MULTISIG_FIELD_NUMBER: _ClassVar[int]
    balance: _containers.RepeatedCompositeFieldContainer[AddressBalance]
    delegated: _containers.RepeatedCompositeFieldContainer[AddressDelegatedBalance]
    total: _containers.RepeatedCompositeFieldContainer[AddressBalance]
    transaction_count: int
    bip_value: str
    locked_stake_until_block: int
    multisig: Multisig
    def __init__(self, balance: _Optional[_Iterable[_Union[AddressBalance, _Mapping]]] = ..., delegated: _Optional[_Iterable[_Union[AddressDelegatedBalance, _Mapping]]] = ..., total: _Optional[_Iterable[_Union[AddressBalance, _Mapping]]] = ..., transaction_count: _Optional[int] = ..., bip_value: _Optional[str] = ..., locked_stake_until_block: _Optional[int] = ..., multisig: _Optional[_Union[Multisig, _Mapping]] = ...) -> None: ...

class Multisig(_message.Message):
    __slots__ = ("threshold", "weights", "addresses")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    weights: _containers.RepeatedScalarFieldContainer[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, threshold: _Optional[int] = ..., weights: _Optional[_Iterable[int]] = ..., addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class AddressesRequest(_message.Message):
    __slots__ = ("addresses", "height", "delegated")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    height: int
    delegated: bool
    def __init__(self, addresses: _Optional[_Iterable[str]] = ..., height: _Optional[int] = ..., delegated: bool = ...) -> None: ...

class AddressesResponse(_message.Message):
    __slots__ = ("addresses",)
    class Result(_message.Message):
        __slots__ = ("balance", "delegated", "total", "transaction_count", "bip_value", "locked_stake_until_block", "multisig")
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        DELEGATED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
        LOCKED_STAKE_UNTIL_BLOCK_FIELD_NUMBER: _ClassVar[int]
        MULTISIG_FIELD_NUMBER: _ClassVar[int]
        balance: _containers.RepeatedCompositeFieldContainer[AddressBalance]
        delegated: _containers.RepeatedCompositeFieldContainer[AddressDelegatedBalance]
        total: _containers.RepeatedCompositeFieldContainer[AddressBalance]
        transaction_count: int
        bip_value: str
        locked_stake_until_block: int
        multisig: Multisig
        def __init__(self, balance: _Optional[_Iterable[_Union[AddressBalance, _Mapping]]] = ..., delegated: _Optional[_Iterable[_Union[AddressDelegatedBalance, _Mapping]]] = ..., total: _Optional[_Iterable[_Union[AddressBalance, _Mapping]]] = ..., transaction_count: _Optional[int] = ..., bip_value: _Optional[str] = ..., locked_stake_until_block: _Optional[int] = ..., multisig: _Optional[_Union[Multisig, _Mapping]] = ...) -> None: ...
    class AddressesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AddressesResponse.Result
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AddressesResponse.Result, _Mapping]] = ...) -> None: ...
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.MessageMap[str, AddressesResponse.Result]
    def __init__(self, addresses: _Optional[_Mapping[str, AddressesResponse.Result]] = ...) -> None: ...

class CandidateRequest(_message.Message):
    __slots__ = ("public_key", "height", "not_show_stakes")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NOT_SHOW_STAKES_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    height: int
    not_show_stakes: bool
    def __init__(self, public_key: _Optional[str] = ..., height: _Optional[int] = ..., not_show_stakes: bool = ...) -> None: ...

class CandidateResponse(_message.Message):
    __slots__ = ("id", "reward_address", "owner_address", "control_address", "total_stake", "public_key", "commission", "used_slots", "uniq_users", "min_stake", "stakes", "status", "validator", "jailed_until")
    class Stake(_message.Message):
        __slots__ = ("owner", "coin", "value", "bip_value")
        OWNER_FIELD_NUMBER: _ClassVar[int]
        COIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        BIP_VALUE_FIELD_NUMBER: _ClassVar[int]
        owner: str
        coin: Coin
        value: str
        bip_value: str
        def __init__(self, owner: _Optional[str] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ..., bip_value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STAKE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    USED_SLOTS_FIELD_NUMBER: _ClassVar[int]
    UNIQ_USERS_FIELD_NUMBER: _ClassVar[int]
    MIN_STAKE_FIELD_NUMBER: _ClassVar[int]
    STAKES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    JAILED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    reward_address: str
    owner_address: str
    control_address: str
    total_stake: str
    public_key: str
    commission: int
    used_slots: _wrappers_pb2.UInt64Value
    uniq_users: _wrappers_pb2.UInt64Value
    min_stake: _wrappers_pb2.StringValue
    stakes: _containers.RepeatedCompositeFieldContainer[CandidateResponse.Stake]
    status: int
    validator: bool
    jailed_until: int
    def __init__(self, id: _Optional[int] = ..., reward_address: _Optional[str] = ..., owner_address: _Optional[str] = ..., control_address: _Optional[str] = ..., total_stake: _Optional[str] = ..., public_key: _Optional[str] = ..., commission: _Optional[int] = ..., used_slots: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., uniq_users: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., min_stake: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stakes: _Optional[_Iterable[_Union[CandidateResponse.Stake, _Mapping]]] = ..., status: _Optional[int] = ..., validator: bool = ..., jailed_until: _Optional[int] = ...) -> None: ...

class CandidatesRequest(_message.Message):
    __slots__ = ("height", "include_stakes", "not_show_stakes", "status")
    class CandidateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        all: _ClassVar[CandidatesRequest.CandidateStatus]
        off: _ClassVar[CandidatesRequest.CandidateStatus]
        on: _ClassVar[CandidatesRequest.CandidateStatus]
        validator: _ClassVar[CandidatesRequest.CandidateStatus]
    all: CandidatesRequest.CandidateStatus
    off: CandidatesRequest.CandidateStatus
    on: CandidatesRequest.CandidateStatus
    validator: CandidatesRequest.CandidateStatus
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STAKES_FIELD_NUMBER: _ClassVar[int]
    NOT_SHOW_STAKES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    height: int
    include_stakes: bool
    not_show_stakes: bool
    status: CandidatesRequest.CandidateStatus
    def __init__(self, height: _Optional[int] = ..., include_stakes: bool = ..., not_show_stakes: bool = ..., status: _Optional[_Union[CandidatesRequest.CandidateStatus, str]] = ...) -> None: ...

class CandidatesResponse(_message.Message):
    __slots__ = ("candidates",)
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[CandidateResponse]
    def __init__(self, candidates: _Optional[_Iterable[_Union[CandidateResponse, _Mapping]]] = ...) -> None: ...

class CoinIdRequest(_message.Message):
    __slots__ = ("height", "id")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    height: int
    id: int
    def __init__(self, height: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class CoinInfoRequest(_message.Message):
    __slots__ = ("height", "symbol")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    height: int
    symbol: str
    def __init__(self, height: _Optional[int] = ..., symbol: _Optional[str] = ...) -> None: ...

class CoinInfoResponse(_message.Message):
    __slots__ = ("id", "name", "symbol", "volume", "crr", "reserve_balance", "max_supply", "owner_address", "mintable", "burnable")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    CRR_FIELD_NUMBER: _ClassVar[int]
    RESERVE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MINTABLE_FIELD_NUMBER: _ClassVar[int]
    BURNABLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    symbol: str
    volume: str
    crr: int
    reserve_balance: str
    max_supply: str
    owner_address: _wrappers_pb2.StringValue
    mintable: bool
    burnable: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., volume: _Optional[str] = ..., crr: _Optional[int] = ..., reserve_balance: _Optional[str] = ..., max_supply: _Optional[str] = ..., owner_address: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mintable: bool = ..., burnable: bool = ...) -> None: ...

class SendTransactionResponse(_message.Message):
    __slots__ = ("code", "log", "hash")
    CODE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    code: int
    log: str
    hash: str
    def __init__(self, code: _Optional[int] = ..., log: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class SendTransactionRequest(_message.Message):
    __slots__ = ("tx",)
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: str
    def __init__(self, tx: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ("hash", "raw_tx", "height", "index", "nonce", "gas", "gas_price", "gas_coin", "type_hex", "type", "data", "payload", "service_data", "tags", "code", "log")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        None: _ClassVar[TransactionResponse.Type]
        Send: _ClassVar[TransactionResponse.Type]
        SellCoin: _ClassVar[TransactionResponse.Type]
        SellAllCoin: _ClassVar[TransactionResponse.Type]
        BuyCoin: _ClassVar[TransactionResponse.Type]
        CreateCoin: _ClassVar[TransactionResponse.Type]
        DeclareCandidacy: _ClassVar[TransactionResponse.Type]
        Delegate: _ClassVar[TransactionResponse.Type]
        Unbond: _ClassVar[TransactionResponse.Type]
        RedeemCheck: _ClassVar[TransactionResponse.Type]
        SetCandidateOnline: _ClassVar[TransactionResponse.Type]
        SetCandidateOffline: _ClassVar[TransactionResponse.Type]
        CreateMultisig: _ClassVar[TransactionResponse.Type]
        Multisend: _ClassVar[TransactionResponse.Type]
        EditCandidate: _ClassVar[TransactionResponse.Type]
        SetHaltBlock: _ClassVar[TransactionResponse.Type]
        RecreateCoin: _ClassVar[TransactionResponse.Type]
        EditCoinOwner: _ClassVar[TransactionResponse.Type]
        EditMultisig: _ClassVar[TransactionResponse.Type]
        PriceVote: _ClassVar[TransactionResponse.Type]
        EditCandidatePublicKey: _ClassVar[TransactionResponse.Type]
        AddLiquidity: _ClassVar[TransactionResponse.Type]
        RemoveLiquidity: _ClassVar[TransactionResponse.Type]
        SellSwapPool: _ClassVar[TransactionResponse.Type]
        BuySwapPool: _ClassVar[TransactionResponse.Type]
        SellAllSwapPool: _ClassVar[TransactionResponse.Type]
        EditCommissionCandidate: _ClassVar[TransactionResponse.Type]
        MoveStake: _ClassVar[TransactionResponse.Type]
        MintToken: _ClassVar[TransactionResponse.Type]
        BurnToken: _ClassVar[TransactionResponse.Type]
        CreateToken: _ClassVar[TransactionResponse.Type]
        RecreateToken: _ClassVar[TransactionResponse.Type]
        VoteCommission: _ClassVar[TransactionResponse.Type]
        VoteUpdate: _ClassVar[TransactionResponse.Type]
        CreateSwapPool: _ClassVar[TransactionResponse.Type]
        AddLimitOrder: _ClassVar[TransactionResponse.Type]
        RemoveLimitOrder: _ClassVar[TransactionResponse.Type]
        TypeLockStake: _ClassVar[TransactionResponse.Type]
        TypeLock: _ClassVar[TransactionResponse.Type]
    None: TransactionResponse.Type
    Send: TransactionResponse.Type
    SellCoin: TransactionResponse.Type
    SellAllCoin: TransactionResponse.Type
    BuyCoin: TransactionResponse.Type
    CreateCoin: TransactionResponse.Type
    DeclareCandidacy: TransactionResponse.Type
    Delegate: TransactionResponse.Type
    Unbond: TransactionResponse.Type
    RedeemCheck: TransactionResponse.Type
    SetCandidateOnline: TransactionResponse.Type
    SetCandidateOffline: TransactionResponse.Type
    CreateMultisig: TransactionResponse.Type
    Multisend: TransactionResponse.Type
    EditCandidate: TransactionResponse.Type
    SetHaltBlock: TransactionResponse.Type
    RecreateCoin: TransactionResponse.Type
    EditCoinOwner: TransactionResponse.Type
    EditMultisig: TransactionResponse.Type
    PriceVote: TransactionResponse.Type
    EditCandidatePublicKey: TransactionResponse.Type
    AddLiquidity: TransactionResponse.Type
    RemoveLiquidity: TransactionResponse.Type
    SellSwapPool: TransactionResponse.Type
    BuySwapPool: TransactionResponse.Type
    SellAllSwapPool: TransactionResponse.Type
    EditCommissionCandidate: TransactionResponse.Type
    MoveStake: TransactionResponse.Type
    MintToken: TransactionResponse.Type
    BurnToken: TransactionResponse.Type
    CreateToken: TransactionResponse.Type
    RecreateToken: TransactionResponse.Type
    VoteCommission: TransactionResponse.Type
    VoteUpdate: TransactionResponse.Type
    CreateSwapPool: TransactionResponse.Type
    AddLimitOrder: TransactionResponse.Type
    RemoveLimitOrder: TransactionResponse.Type
    TypeLockStake: TransactionResponse.Type
    TypeLock: TransactionResponse.Type
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HASH_FIELD_NUMBER: _ClassVar[int]
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    GAS_COIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_HEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    hash: str
    raw_tx: str
    height: int
    index: int
    nonce: int
    gas: int
    gas_price: int
    gas_coin: Coin
    type_hex: str
    type: int
    data: _any_pb2.Any
    payload: bytes
    service_data: bytes
    tags: _containers.ScalarMap[str, str]
    code: int
    log: str
    def __init__(self, hash: _Optional[str] = ..., raw_tx: _Optional[str] = ..., height: _Optional[int] = ..., index: _Optional[int] = ..., nonce: _Optional[int] = ..., gas: _Optional[int] = ..., gas_price: _Optional[int] = ..., gas_coin: _Optional[_Union[Coin, _Mapping]] = ..., type_hex: _Optional[str] = ..., type: _Optional[int] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., payload: _Optional[bytes] = ..., service_data: _Optional[bytes] = ..., tags: _Optional[_Mapping[str, str]] = ..., code: _Optional[int] = ..., log: _Optional[str] = ..., **kwargs) -> None: ...

class TransactionRequest(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class TransactionsResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[TransactionResponse]
    def __init__(self, transactions: _Optional[_Iterable[_Union[TransactionResponse, _Mapping]]] = ...) -> None: ...

class TransactionsRequest(_message.Message):
    __slots__ = ("query", "page", "per_page")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    query: str
    page: int
    per_page: int
    def __init__(self, query: _Optional[str] = ..., page: _Optional[int] = ..., per_page: _Optional[int] = ...) -> None: ...

class EstimateCoinBuyRequest(_message.Message):
    __slots__ = ("coin_id_to_buy", "coin_to_buy", "coin_id_to_sell", "coin_to_sell", "value_to_buy", "height", "coin_id_commission", "coin_commission", "swap_from", "route")
    COIN_ID_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_ID_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    COIN_ID_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    COIN_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    SWAP_FROM_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    coin_id_to_buy: int
    coin_to_buy: str
    coin_id_to_sell: int
    coin_to_sell: str
    value_to_buy: str
    height: int
    coin_id_commission: int
    coin_commission: str
    swap_from: SwapFrom
    route: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, coin_id_to_buy: _Optional[int] = ..., coin_to_buy: _Optional[str] = ..., coin_id_to_sell: _Optional[int] = ..., coin_to_sell: _Optional[str] = ..., value_to_buy: _Optional[str] = ..., height: _Optional[int] = ..., coin_id_commission: _Optional[int] = ..., coin_commission: _Optional[str] = ..., swap_from: _Optional[_Union[SwapFrom, str]] = ..., route: _Optional[_Iterable[int]] = ...) -> None: ...

class EstimateCoinBuyResponse(_message.Message):
    __slots__ = ("will_pay", "commission", "swap_from")
    WILL_PAY_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    SWAP_FROM_FIELD_NUMBER: _ClassVar[int]
    will_pay: str
    commission: str
    swap_from: SwapFrom
    def __init__(self, will_pay: _Optional[str] = ..., commission: _Optional[str] = ..., swap_from: _Optional[_Union[SwapFrom, str]] = ...) -> None: ...

class EstimateCoinSellRequest(_message.Message):
    __slots__ = ("coin_id_to_buy", "coin_to_buy", "coin_id_to_sell", "coin_to_sell", "value_to_sell", "height", "coin_id_commission", "coin_commission", "swap_from", "route")
    COIN_ID_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_ID_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    COIN_ID_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    COIN_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    SWAP_FROM_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    coin_id_to_buy: int
    coin_to_buy: str
    coin_id_to_sell: int
    coin_to_sell: str
    value_to_sell: str
    height: int
    coin_id_commission: int
    coin_commission: str
    swap_from: SwapFrom
    route: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, coin_id_to_buy: _Optional[int] = ..., coin_to_buy: _Optional[str] = ..., coin_id_to_sell: _Optional[int] = ..., coin_to_sell: _Optional[str] = ..., value_to_sell: _Optional[str] = ..., height: _Optional[int] = ..., coin_id_commission: _Optional[int] = ..., coin_commission: _Optional[str] = ..., swap_from: _Optional[_Union[SwapFrom, str]] = ..., route: _Optional[_Iterable[int]] = ...) -> None: ...

class EstimateCoinSellResponse(_message.Message):
    __slots__ = ("will_get", "commission", "swap_from")
    WILL_GET_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    SWAP_FROM_FIELD_NUMBER: _ClassVar[int]
    will_get: str
    commission: str
    swap_from: SwapFrom
    def __init__(self, will_get: _Optional[str] = ..., commission: _Optional[str] = ..., swap_from: _Optional[_Union[SwapFrom, str]] = ...) -> None: ...

class EstimateCoinSellAllRequest(_message.Message):
    __slots__ = ("coin_id_to_buy", "coin_to_buy", "coin_id_to_sell", "coin_to_sell", "value_to_sell", "gas_price", "height", "swap_from", "route")
    COIN_ID_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_ID_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SWAP_FROM_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    coin_id_to_buy: int
    coin_to_buy: str
    coin_id_to_sell: int
    coin_to_sell: str
    value_to_sell: str
    gas_price: int
    height: int
    swap_from: SwapFrom
    route: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, coin_id_to_buy: _Optional[int] = ..., coin_to_buy: _Optional[str] = ..., coin_id_to_sell: _Optional[int] = ..., coin_to_sell: _Optional[str] = ..., value_to_sell: _Optional[str] = ..., gas_price: _Optional[int] = ..., height: _Optional[int] = ..., swap_from: _Optional[_Union[SwapFrom, str]] = ..., route: _Optional[_Iterable[int]] = ...) -> None: ...

class EstimateCoinSellAllResponse(_message.Message):
    __slots__ = ("will_get", "swap_from")
    WILL_GET_FIELD_NUMBER: _ClassVar[int]
    SWAP_FROM_FIELD_NUMBER: _ClassVar[int]
    will_get: str
    swap_from: SwapFrom
    def __init__(self, will_get: _Optional[str] = ..., swap_from: _Optional[_Union[SwapFrom, str]] = ...) -> None: ...

class EstimateTxCommissionRequest(_message.Message):
    __slots__ = ("tx", "height")
    TX_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    tx: str
    height: int
    def __init__(self, tx: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class EstimateTxCommissionResponse(_message.Message):
    __slots__ = ("commission",)
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    commission: str
    def __init__(self, commission: _Optional[str] = ...) -> None: ...

class EventsRequest(_message.Message):
    __slots__ = ("height", "search")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    height: int
    search: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, height: _Optional[int] = ..., search: _Optional[_Iterable[str]] = ...) -> None: ...

class EventsResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, events: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class MissedBlocksRequest(_message.Message):
    __slots__ = ("public_key", "height")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    height: int
    def __init__(self, public_key: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class MissedBlocksResponse(_message.Message):
    __slots__ = ("missed_blocks", "missed_blocks_count")
    MISSED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    MISSED_BLOCKS_COUNT_FIELD_NUMBER: _ClassVar[int]
    missed_blocks: str
    missed_blocks_count: int
    def __init__(self, missed_blocks: _Optional[str] = ..., missed_blocks_count: _Optional[int] = ...) -> None: ...

class UnconfirmedTxsResponse(_message.Message):
    __slots__ = ("transaction_count", "total_transactions", "total_bytes", "transactions")
    TRANSACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transaction_count: int
    total_transactions: int
    total_bytes: int
    transactions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transaction_count: _Optional[int] = ..., total_transactions: _Optional[int] = ..., total_bytes: _Optional[int] = ..., transactions: _Optional[_Iterable[str]] = ...) -> None: ...

class UnconfirmedTxsRequest(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class ValidatorsRequest(_message.Message):
    __slots__ = ("height",)
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class ValidatorsResponse(_message.Message):
    __slots__ = ("validators",)
    class Result(_message.Message):
        __slots__ = ("public_key", "voting_power")
        PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        VOTING_POWER_FIELD_NUMBER: _ClassVar[int]
        public_key: str
        voting_power: int
        def __init__(self, public_key: _Optional[str] = ..., voting_power: _Optional[int] = ...) -> None: ...
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    validators: _containers.RepeatedCompositeFieldContainer[ValidatorsResponse.Result]
    def __init__(self, validators: _Optional[_Iterable[_Union[ValidatorsResponse.Result, _Mapping]]] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ("query", "data", "events")
    class Event(_message.Message):
        __slots__ = ("key", "events")
        KEY_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        key: str
        events: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[str] = ..., events: _Optional[_Iterable[str]] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    query: str
    data: _struct_pb2.Struct
    events: _containers.RepeatedCompositeFieldContainer[SubscribeResponse.Event]
    def __init__(self, query: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., events: _Optional[_Iterable[_Union[SubscribeResponse.Event, _Mapping]]] = ...) -> None: ...

class HaltsRequest(_message.Message):
    __slots__ = ("height",)
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class HaltsResponse(_message.Message):
    __slots__ = ("public_keys",)
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    public_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, public_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class FrozenRequest(_message.Message):
    __slots__ = ("address", "coin_id", "height")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COIN_ID_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    address: str
    coin_id: _wrappers_pb2.UInt64Value
    height: int
    def __init__(self, address: _Optional[str] = ..., coin_id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., height: _Optional[int] = ...) -> None: ...

class FrozenAllRequest(_message.Message):
    __slots__ = ("start_height", "end_height", "height", "addresses", "coin_ids")
    START_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    END_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    COIN_IDS_FIELD_NUMBER: _ClassVar[int]
    start_height: int
    end_height: int
    height: int
    addresses: _containers.RepeatedScalarFieldContainer[str]
    coin_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, start_height: _Optional[int] = ..., end_height: _Optional[int] = ..., height: _Optional[int] = ..., addresses: _Optional[_Iterable[str]] = ..., coin_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class FrozenResponse(_message.Message):
    __slots__ = ("frozen",)
    class Frozen(_message.Message):
        __slots__ = ("height", "address", "candidate_key", "coin", "value", "move_to_candidate_key")
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
        COIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        MOVE_TO_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
        height: int
        address: str
        candidate_key: _wrappers_pb2.StringValue
        coin: Coin
        value: str
        move_to_candidate_key: _wrappers_pb2.StringValue
        def __init__(self, height: _Optional[int] = ..., address: _Optional[str] = ..., candidate_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ..., move_to_candidate_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    frozen: _containers.RepeatedCompositeFieldContainer[FrozenResponse.Frozen]
    def __init__(self, frozen: _Optional[_Iterable[_Union[FrozenResponse.Frozen, _Mapping]]] = ...) -> None: ...

class WaitListRequest(_message.Message):
    __slots__ = ("public_key", "address", "height")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    address: str
    height: int
    def __init__(self, public_key: _Optional[str] = ..., address: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class WaitListResponse(_message.Message):
    __slots__ = ("list",)
    class Wait(_message.Message):
        __slots__ = ("public_key", "coin", "value")
        PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
        COIN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        public_key: str
        coin: Coin
        value: str
        def __init__(self, public_key: _Optional[str] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...
    LIST_FIELD_NUMBER: _ClassVar[int]
    list: _containers.RepeatedCompositeFieldContainer[WaitListResponse.Wait]
    def __init__(self, list: _Optional[_Iterable[_Union[WaitListResponse.Wait, _Mapping]]] = ...) -> None: ...

class SendData(_message.Message):
    __slots__ = ("coin", "to", "value")
    COIN_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    coin: Coin
    to: str
    value: str
    def __init__(self, coin: _Optional[_Union[Coin, _Mapping]] = ..., to: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SellCoinData(_message.Message):
    __slots__ = ("coin_to_sell", "value_to_sell", "coin_to_buy", "minimum_value_to_buy")
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    coin_to_sell: Coin
    value_to_sell: str
    coin_to_buy: Coin
    minimum_value_to_buy: str
    def __init__(self, coin_to_sell: _Optional[_Union[Coin, _Mapping]] = ..., value_to_sell: _Optional[str] = ..., coin_to_buy: _Optional[_Union[Coin, _Mapping]] = ..., minimum_value_to_buy: _Optional[str] = ...) -> None: ...

class SellAllCoinData(_message.Message):
    __slots__ = ("coin_to_sell", "coin_to_buy", "minimum_value_to_buy")
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    coin_to_sell: Coin
    coin_to_buy: Coin
    minimum_value_to_buy: str
    def __init__(self, coin_to_sell: _Optional[_Union[Coin, _Mapping]] = ..., coin_to_buy: _Optional[_Union[Coin, _Mapping]] = ..., minimum_value_to_buy: _Optional[str] = ...) -> None: ...

class BuyCoinData(_message.Message):
    __slots__ = ("coin_to_buy", "value_to_buy", "coin_to_sell", "maximum_value_to_sell")
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    coin_to_buy: Coin
    value_to_buy: str
    coin_to_sell: Coin
    maximum_value_to_sell: str
    def __init__(self, coin_to_buy: _Optional[_Union[Coin, _Mapping]] = ..., value_to_buy: _Optional[str] = ..., coin_to_sell: _Optional[_Union[Coin, _Mapping]] = ..., maximum_value_to_sell: _Optional[str] = ...) -> None: ...

class CreateCoinData(_message.Message):
    __slots__ = ("name", "symbol", "initial_amount", "initial_reserve", "constant_reserve_ratio", "max_supply")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_RESERVE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_RESERVE_RATIO_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    symbol: str
    initial_amount: str
    initial_reserve: str
    constant_reserve_ratio: int
    max_supply: str
    def __init__(self, name: _Optional[str] = ..., symbol: _Optional[str] = ..., initial_amount: _Optional[str] = ..., initial_reserve: _Optional[str] = ..., constant_reserve_ratio: _Optional[int] = ..., max_supply: _Optional[str] = ...) -> None: ...

class DeclareCandidacyData(_message.Message):
    __slots__ = ("address", "pub_key", "commission", "coin", "stake")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    STAKE_FIELD_NUMBER: _ClassVar[int]
    address: str
    pub_key: str
    commission: int
    coin: Coin
    stake: str
    def __init__(self, address: _Optional[str] = ..., pub_key: _Optional[str] = ..., commission: _Optional[int] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., stake: _Optional[str] = ...) -> None: ...

class DelegateData(_message.Message):
    __slots__ = ("pub_key", "coin", "value")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    coin: Coin
    value: str
    def __init__(self, pub_key: _Optional[str] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class UnbondData(_message.Message):
    __slots__ = ("pub_key", "coin", "value")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    coin: Coin
    value: str
    def __init__(self, pub_key: _Optional[str] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class RedeemCheckData(_message.Message):
    __slots__ = ("raw_check", "proof")
    RAW_CHECK_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    raw_check: str
    proof: str
    def __init__(self, raw_check: _Optional[str] = ..., proof: _Optional[str] = ...) -> None: ...

class SetCandidateOnData(_message.Message):
    __slots__ = ("pub_key",)
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    def __init__(self, pub_key: _Optional[str] = ...) -> None: ...

class SetCandidateOffData(_message.Message):
    __slots__ = ("pub_key",)
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    def __init__(self, pub_key: _Optional[str] = ...) -> None: ...

class CreateMultisigData(_message.Message):
    __slots__ = ("threshold", "weights", "addresses")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    weights: _containers.RepeatedScalarFieldContainer[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, threshold: _Optional[int] = ..., weights: _Optional[_Iterable[int]] = ..., addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class MultiSendData(_message.Message):
    __slots__ = ("list",)
    LIST_FIELD_NUMBER: _ClassVar[int]
    list: _containers.RepeatedCompositeFieldContainer[SendData]
    def __init__(self, list: _Optional[_Iterable[_Union[SendData, _Mapping]]] = ...) -> None: ...

class EditCandidateData(_message.Message):
    __slots__ = ("pub_key", "reward_address", "owner_address", "control_address")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    REWARD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OWNER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    reward_address: str
    owner_address: str
    control_address: str
    def __init__(self, pub_key: _Optional[str] = ..., reward_address: _Optional[str] = ..., owner_address: _Optional[str] = ..., control_address: _Optional[str] = ...) -> None: ...

class SetHaltBlockData(_message.Message):
    __slots__ = ("pub_key", "height")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    height: int
    def __init__(self, pub_key: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class RecreateCoinData(_message.Message):
    __slots__ = ("name", "symbol", "initial_amount", "initial_reserve", "constant_reserve_ratio", "max_supply")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_RESERVE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_RESERVE_RATIO_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    symbol: str
    initial_amount: str
    initial_reserve: str
    constant_reserve_ratio: int
    max_supply: str
    def __init__(self, name: _Optional[str] = ..., symbol: _Optional[str] = ..., initial_amount: _Optional[str] = ..., initial_reserve: _Optional[str] = ..., constant_reserve_ratio: _Optional[int] = ..., max_supply: _Optional[str] = ...) -> None: ...

class EditCoinOwnerData(_message.Message):
    __slots__ = ("symbol", "new_owner")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NEW_OWNER_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    new_owner: str
    def __init__(self, symbol: _Optional[str] = ..., new_owner: _Optional[str] = ...) -> None: ...

class EditMultisigData(_message.Message):
    __slots__ = ("threshold", "weights", "addresses")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    weights: _containers.RepeatedScalarFieldContainer[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, threshold: _Optional[int] = ..., weights: _Optional[_Iterable[int]] = ..., addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class EditCandidatePublicKeyData(_message.Message):
    __slots__ = ("pub_key", "new_pub_key")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    NEW_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    new_pub_key: str
    def __init__(self, pub_key: _Optional[str] = ..., new_pub_key: _Optional[str] = ...) -> None: ...

class CreateSwapPoolData(_message.Message):
    __slots__ = ("coin0", "coin1", "volume0", "volume1")
    COIN0_FIELD_NUMBER: _ClassVar[int]
    COIN1_FIELD_NUMBER: _ClassVar[int]
    VOLUME0_FIELD_NUMBER: _ClassVar[int]
    VOLUME1_FIELD_NUMBER: _ClassVar[int]
    coin0: Coin
    coin1: Coin
    volume0: str
    volume1: str
    def __init__(self, coin0: _Optional[_Union[Coin, _Mapping]] = ..., coin1: _Optional[_Union[Coin, _Mapping]] = ..., volume0: _Optional[str] = ..., volume1: _Optional[str] = ...) -> None: ...

class AddLiquidityData(_message.Message):
    __slots__ = ("coin0", "coin1", "volume0", "maximum_volume1")
    COIN0_FIELD_NUMBER: _ClassVar[int]
    COIN1_FIELD_NUMBER: _ClassVar[int]
    VOLUME0_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VOLUME1_FIELD_NUMBER: _ClassVar[int]
    coin0: Coin
    coin1: Coin
    volume0: str
    maximum_volume1: str
    def __init__(self, coin0: _Optional[_Union[Coin, _Mapping]] = ..., coin1: _Optional[_Union[Coin, _Mapping]] = ..., volume0: _Optional[str] = ..., maximum_volume1: _Optional[str] = ...) -> None: ...

class RemoveLiquidityData(_message.Message):
    __slots__ = ("coin0", "coin1", "liquidity", "minimum_volume0", "minimum_volume1")
    COIN0_FIELD_NUMBER: _ClassVar[int]
    COIN1_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VOLUME0_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VOLUME1_FIELD_NUMBER: _ClassVar[int]
    coin0: Coin
    coin1: Coin
    liquidity: str
    minimum_volume0: str
    minimum_volume1: str
    def __init__(self, coin0: _Optional[_Union[Coin, _Mapping]] = ..., coin1: _Optional[_Union[Coin, _Mapping]] = ..., liquidity: _Optional[str] = ..., minimum_volume0: _Optional[str] = ..., minimum_volume1: _Optional[str] = ...) -> None: ...

class SellSwapPoolData(_message.Message):
    __slots__ = ("coins", "value_to_sell", "minimum_value_to_buy")
    COINS_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[Coin]
    value_to_sell: str
    minimum_value_to_buy: str
    def __init__(self, coins: _Optional[_Iterable[_Union[Coin, _Mapping]]] = ..., value_to_sell: _Optional[str] = ..., minimum_value_to_buy: _Optional[str] = ...) -> None: ...

class SellAllSwapPoolData(_message.Message):
    __slots__ = ("coins", "minimum_value_to_buy")
    COINS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[Coin]
    minimum_value_to_buy: str
    def __init__(self, coins: _Optional[_Iterable[_Union[Coin, _Mapping]]] = ..., minimum_value_to_buy: _Optional[str] = ...) -> None: ...

class BuySwapPoolData(_message.Message):
    __slots__ = ("coins", "value_to_buy", "maximum_value_to_sell")
    COINS_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    coins: _containers.RepeatedCompositeFieldContainer[Coin]
    value_to_buy: str
    maximum_value_to_sell: str
    def __init__(self, coins: _Optional[_Iterable[_Union[Coin, _Mapping]]] = ..., value_to_buy: _Optional[str] = ..., maximum_value_to_sell: _Optional[str] = ...) -> None: ...

class EditCandidateCommission(_message.Message):
    __slots__ = ("pub_key", "commission")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    commission: int
    def __init__(self, pub_key: _Optional[str] = ..., commission: _Optional[int] = ...) -> None: ...

class MintTokenData(_message.Message):
    __slots__ = ("coin", "value")
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    coin: Coin
    value: str
    def __init__(self, coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class BurnTokenData(_message.Message):
    __slots__ = ("coin", "value")
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    coin: Coin
    value: str
    def __init__(self, coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class CreateTokenData(_message.Message):
    __slots__ = ("name", "symbol", "initial_amount", "max_supply", "mintable", "burnable")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    MINTABLE_FIELD_NUMBER: _ClassVar[int]
    BURNABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    symbol: str
    initial_amount: str
    max_supply: str
    mintable: bool
    burnable: bool
    def __init__(self, name: _Optional[str] = ..., symbol: _Optional[str] = ..., initial_amount: _Optional[str] = ..., max_supply: _Optional[str] = ..., mintable: bool = ..., burnable: bool = ...) -> None: ...

class RecreateTokenData(_message.Message):
    __slots__ = ("name", "symbol", "initial_amount", "max_supply", "mintable", "burnable")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPLY_FIELD_NUMBER: _ClassVar[int]
    MINTABLE_FIELD_NUMBER: _ClassVar[int]
    BURNABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    symbol: str
    initial_amount: str
    max_supply: str
    mintable: bool
    burnable: bool
    def __init__(self, name: _Optional[str] = ..., symbol: _Optional[str] = ..., initial_amount: _Optional[str] = ..., max_supply: _Optional[str] = ..., mintable: bool = ..., burnable: bool = ...) -> None: ...

class VoteCommissionData(_message.Message):
    __slots__ = ("pub_key", "height", "coin", "payload_byte", "send", "buy_bancor", "sell_bancor", "sell_all_bancor", "buy_pool_base", "buy_pool_delta", "sell_pool_base", "sell_pool_delta", "sell_all_pool_base", "sell_all_pool_delta", "create_ticker3", "create_ticker4", "create_ticker5", "create_ticker6", "create_ticker7_10", "create_coin", "create_token", "recreate_coin", "recreate_token", "declare_candidacy", "delegate", "unbond", "redeem_check", "set_candidate_on", "set_candidate_off", "create_multisig", "multisend_base", "multisend_delta", "edit_candidate", "set_halt_block", "edit_ticker_owner", "edit_multisig", "edit_candidate_public_key", "create_swap_pool", "add_liquidity", "remove_liquidity", "edit_candidate_commission", "mint_token", "burn_token", "vote_commission", "vote_update", "failed_tx", "add_limit_order", "remove_limit_order", "move_stake", "lock_stake", "lock")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_BYTE_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    BUY_BANCOR_FIELD_NUMBER: _ClassVar[int]
    SELL_BANCOR_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_BANCOR_FIELD_NUMBER: _ClassVar[int]
    BUY_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    BUY_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    SELL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    SELL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER3_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER4_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER5_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER6_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER7_10_FIELD_NUMBER: _ClassVar[int]
    CREATE_COIN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECREATE_COIN_FIELD_NUMBER: _ClassVar[int]
    RECREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DECLARE_CANDIDACY_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_FIELD_NUMBER: _ClassVar[int]
    UNBOND_FIELD_NUMBER: _ClassVar[int]
    REDEEM_CHECK_FIELD_NUMBER: _ClassVar[int]
    SET_CANDIDATE_ON_FIELD_NUMBER: _ClassVar[int]
    SET_CANDIDATE_OFF_FIELD_NUMBER: _ClassVar[int]
    CREATE_MULTISIG_FIELD_NUMBER: _ClassVar[int]
    MULTISEND_BASE_FIELD_NUMBER: _ClassVar[int]
    MULTISEND_DELTA_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    SET_HALT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    EDIT_TICKER_OWNER_FIELD_NUMBER: _ClassVar[int]
    EDIT_MULTISIG_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_SWAP_POOL_FIELD_NUMBER: _ClassVar[int]
    ADD_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    MINT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BURN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VOTE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    VOTE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    FAILED_TX_FIELD_NUMBER: _ClassVar[int]
    ADD_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
    MOVE_STAKE_FIELD_NUMBER: _ClassVar[int]
    LOCK_STAKE_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    height: int
    coin: Coin
    payload_byte: str
    send: str
    buy_bancor: str
    sell_bancor: str
    sell_all_bancor: str
    buy_pool_base: str
    buy_pool_delta: str
    sell_pool_base: str
    sell_pool_delta: str
    sell_all_pool_base: str
    sell_all_pool_delta: str
    create_ticker3: str
    create_ticker4: str
    create_ticker5: str
    create_ticker6: str
    create_ticker7_10: str
    create_coin: str
    create_token: str
    recreate_coin: str
    recreate_token: str
    declare_candidacy: str
    delegate: str
    unbond: str
    redeem_check: str
    set_candidate_on: str
    set_candidate_off: str
    create_multisig: str
    multisend_base: str
    multisend_delta: str
    edit_candidate: str
    set_halt_block: str
    edit_ticker_owner: str
    edit_multisig: str
    edit_candidate_public_key: str
    create_swap_pool: str
    add_liquidity: str
    remove_liquidity: str
    edit_candidate_commission: str
    mint_token: str
    burn_token: str
    vote_commission: str
    vote_update: str
    failed_tx: str
    add_limit_order: str
    remove_limit_order: str
    move_stake: str
    lock_stake: str
    lock: str
    def __init__(self, pub_key: _Optional[str] = ..., height: _Optional[int] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., payload_byte: _Optional[str] = ..., send: _Optional[str] = ..., buy_bancor: _Optional[str] = ..., sell_bancor: _Optional[str] = ..., sell_all_bancor: _Optional[str] = ..., buy_pool_base: _Optional[str] = ..., buy_pool_delta: _Optional[str] = ..., sell_pool_base: _Optional[str] = ..., sell_pool_delta: _Optional[str] = ..., sell_all_pool_base: _Optional[str] = ..., sell_all_pool_delta: _Optional[str] = ..., create_ticker3: _Optional[str] = ..., create_ticker4: _Optional[str] = ..., create_ticker5: _Optional[str] = ..., create_ticker6: _Optional[str] = ..., create_ticker7_10: _Optional[str] = ..., create_coin: _Optional[str] = ..., create_token: _Optional[str] = ..., recreate_coin: _Optional[str] = ..., recreate_token: _Optional[str] = ..., declare_candidacy: _Optional[str] = ..., delegate: _Optional[str] = ..., unbond: _Optional[str] = ..., redeem_check: _Optional[str] = ..., set_candidate_on: _Optional[str] = ..., set_candidate_off: _Optional[str] = ..., create_multisig: _Optional[str] = ..., multisend_base: _Optional[str] = ..., multisend_delta: _Optional[str] = ..., edit_candidate: _Optional[str] = ..., set_halt_block: _Optional[str] = ..., edit_ticker_owner: _Optional[str] = ..., edit_multisig: _Optional[str] = ..., edit_candidate_public_key: _Optional[str] = ..., create_swap_pool: _Optional[str] = ..., add_liquidity: _Optional[str] = ..., remove_liquidity: _Optional[str] = ..., edit_candidate_commission: _Optional[str] = ..., mint_token: _Optional[str] = ..., burn_token: _Optional[str] = ..., vote_commission: _Optional[str] = ..., vote_update: _Optional[str] = ..., failed_tx: _Optional[str] = ..., add_limit_order: _Optional[str] = ..., remove_limit_order: _Optional[str] = ..., move_stake: _Optional[str] = ..., lock_stake: _Optional[str] = ..., lock: _Optional[str] = ...) -> None: ...

class VoteUpdateData(_message.Message):
    __slots__ = ("pub_key", "height", "version")
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    pub_key: str
    height: int
    version: str
    def __init__(self, pub_key: _Optional[str] = ..., height: _Optional[int] = ..., version: _Optional[str] = ...) -> None: ...

class AddLimitOrderData(_message.Message):
    __slots__ = ("coin_to_sell", "value_to_sell", "coin_to_buy", "value_to_buy")
    COIN_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_SELL_FIELD_NUMBER: _ClassVar[int]
    COIN_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    VALUE_TO_BUY_FIELD_NUMBER: _ClassVar[int]
    coin_to_sell: Coin
    value_to_sell: str
    coin_to_buy: Coin
    value_to_buy: str
    def __init__(self, coin_to_sell: _Optional[_Union[Coin, _Mapping]] = ..., value_to_sell: _Optional[str] = ..., coin_to_buy: _Optional[_Union[Coin, _Mapping]] = ..., value_to_buy: _Optional[str] = ...) -> None: ...

class RemoveLimitOrderData(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MoveStakeData(_message.Message):
    __slots__ = ("from_pub_key", "to_pub_key", "coin", "value")
    FROM_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    TO_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    from_pub_key: str
    to_pub_key: str
    coin: Coin
    value: str
    def __init__(self, from_pub_key: _Optional[str] = ..., to_pub_key: _Optional[str] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class LockStakeData(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockData(_message.Message):
    __slots__ = ("due_block", "coin", "value")
    DUE_BLOCK_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    due_block: int
    coin: Coin
    value: str
    def __init__(self, due_block: _Optional[int] = ..., coin: _Optional[_Union[Coin, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class JailEvent(_message.Message):
    __slots__ = ("validator_pub_key", "jailed_until")
    VALIDATOR_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    JAILED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    validator_pub_key: str
    jailed_until: int
    def __init__(self, validator_pub_key: _Optional[str] = ..., jailed_until: _Optional[int] = ...) -> None: ...

class RemoveCandidateEvent(_message.Message):
    __slots__ = ("candidate_pub_key",)
    CANDIDATE_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    candidate_pub_key: str
    def __init__(self, candidate_pub_key: _Optional[str] = ...) -> None: ...

class RewardEvent(_message.Message):
    __slots__ = ("role", "address", "amount", "validator_pub_key", "for_coin")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Validator: _ClassVar[RewardEvent.Role]
        Delegator: _ClassVar[RewardEvent.Role]
        DAO: _ClassVar[RewardEvent.Role]
        Developers: _ClassVar[RewardEvent.Role]
    Validator: RewardEvent.Role
    Delegator: RewardEvent.Role
    DAO: RewardEvent.Role
    Developers: RewardEvent.Role
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    FOR_COIN_FIELD_NUMBER: _ClassVar[int]
    role: RewardEvent.Role
    address: str
    amount: str
    validator_pub_key: str
    for_coin: int
    def __init__(self, role: _Optional[_Union[RewardEvent.Role, str]] = ..., address: _Optional[str] = ..., amount: _Optional[str] = ..., validator_pub_key: _Optional[str] = ..., for_coin: _Optional[int] = ...) -> None: ...

class SlashEvent(_message.Message):
    __slots__ = ("address", "amount", "coin", "validator_pub_key")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    coin: int
    validator_pub_key: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., coin: _Optional[int] = ..., validator_pub_key: _Optional[str] = ...) -> None: ...

class UnbondEvent(_message.Message):
    __slots__ = ("address", "amount", "coin", "validator_pub_key")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    coin: int
    validator_pub_key: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., coin: _Optional[int] = ..., validator_pub_key: _Optional[str] = ...) -> None: ...

class StakeKickEvent(_message.Message):
    __slots__ = ("address", "amount", "coin", "validator_pub_key")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    coin: int
    validator_pub_key: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., coin: _Optional[int] = ..., validator_pub_key: _Optional[str] = ...) -> None: ...

class UpdateNetworkEvent(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class UpdateCommissionsEvent(_message.Message):
    __slots__ = ("coin", "payload_byte", "send", "buy_bancor", "sell_bancor", "sell_all_bancor", "buy_pool_base", "buy_pool_delta", "sell_pool_base", "sell_pool_delta", "sell_all_pool_base", "sell_all_pool_delta", "create_ticker3", "create_ticker4", "create_ticker5", "create_ticker6", "create_ticker7_10", "create_coin", "create_token", "recreate_coin", "recreate_token", "declare_candidacy", "delegate", "unbond", "redeem_check", "set_candidate_on", "set_candidate_off", "create_multisig", "multisend_base", "multisend_delta", "edit_candidate", "set_halt_block", "edit_ticker_owner", "edit_multisig", "edit_candidate_public_key", "create_swap_pool", "add_liquidity", "remove_liquidity", "edit_candidate_commission", "mint_token", "burn_token", "vote_commission", "vote_update", "failed_tx", "add_limit_order", "remove_limit_order", "move_stake", "lock_stake", "lock")
    COIN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_BYTE_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    BUY_BANCOR_FIELD_NUMBER: _ClassVar[int]
    SELL_BANCOR_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_BANCOR_FIELD_NUMBER: _ClassVar[int]
    BUY_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    BUY_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    SELL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    SELL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_POOL_BASE_FIELD_NUMBER: _ClassVar[int]
    SELL_ALL_POOL_DELTA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER3_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER4_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER5_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER6_FIELD_NUMBER: _ClassVar[int]
    CREATE_TICKER7_10_FIELD_NUMBER: _ClassVar[int]
    CREATE_COIN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECREATE_COIN_FIELD_NUMBER: _ClassVar[int]
    RECREATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DECLARE_CANDIDACY_FIELD_NUMBER: _ClassVar[int]
    DELEGATE_FIELD_NUMBER: _ClassVar[int]
    UNBOND_FIELD_NUMBER: _ClassVar[int]
    REDEEM_CHECK_FIELD_NUMBER: _ClassVar[int]
    SET_CANDIDATE_ON_FIELD_NUMBER: _ClassVar[int]
    SET_CANDIDATE_OFF_FIELD_NUMBER: _ClassVar[int]
    CREATE_MULTISIG_FIELD_NUMBER: _ClassVar[int]
    MULTISEND_BASE_FIELD_NUMBER: _ClassVar[int]
    MULTISEND_DELTA_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    SET_HALT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    EDIT_TICKER_OWNER_FIELD_NUMBER: _ClassVar[int]
    EDIT_MULTISIG_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_SWAP_POOL_FIELD_NUMBER: _ClassVar[int]
    ADD_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    EDIT_CANDIDATE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    MINT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BURN_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VOTE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    VOTE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    FAILED_TX_FIELD_NUMBER: _ClassVar[int]
    ADD_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LIMIT_ORDER_FIELD_NUMBER: _ClassVar[int]
    MOVE_STAKE_FIELD_NUMBER: _ClassVar[int]
    LOCK_STAKE_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    coin: int
    payload_byte: str
    send: str
    buy_bancor: str
    sell_bancor: str
    sell_all_bancor: str
    buy_pool_base: str
    buy_pool_delta: str
    sell_pool_base: str
    sell_pool_delta: str
    sell_all_pool_base: str
    sell_all_pool_delta: str
    create_ticker3: str
    create_ticker4: str
    create_ticker5: str
    create_ticker6: str
    create_ticker7_10: str
    create_coin: str
    create_token: str
    recreate_coin: str
    recreate_token: str
    declare_candidacy: str
    delegate: str
    unbond: str
    redeem_check: str
    set_candidate_on: str
    set_candidate_off: str
    create_multisig: str
    multisend_base: str
    multisend_delta: str
    edit_candidate: str
    set_halt_block: str
    edit_ticker_owner: str
    edit_multisig: str
    edit_candidate_public_key: str
    create_swap_pool: str
    add_liquidity: str
    remove_liquidity: str
    edit_candidate_commission: str
    mint_token: str
    burn_token: str
    vote_commission: str
    vote_update: str
    failed_tx: str
    add_limit_order: str
    remove_limit_order: str
    move_stake: str
    lock_stake: str
    lock: str
    def __init__(self, coin: _Optional[int] = ..., payload_byte: _Optional[str] = ..., send: _Optional[str] = ..., buy_bancor: _Optional[str] = ..., sell_bancor: _Optional[str] = ..., sell_all_bancor: _Optional[str] = ..., buy_pool_base: _Optional[str] = ..., buy_pool_delta: _Optional[str] = ..., sell_pool_base: _Optional[str] = ..., sell_pool_delta: _Optional[str] = ..., sell_all_pool_base: _Optional[str] = ..., sell_all_pool_delta: _Optional[str] = ..., create_ticker3: _Optional[str] = ..., create_ticker4: _Optional[str] = ..., create_ticker5: _Optional[str] = ..., create_ticker6: _Optional[str] = ..., create_ticker7_10: _Optional[str] = ..., create_coin: _Optional[str] = ..., create_token: _Optional[str] = ..., recreate_coin: _Optional[str] = ..., recreate_token: _Optional[str] = ..., declare_candidacy: _Optional[str] = ..., delegate: _Optional[str] = ..., unbond: _Optional[str] = ..., redeem_check: _Optional[str] = ..., set_candidate_on: _Optional[str] = ..., set_candidate_off: _Optional[str] = ..., create_multisig: _Optional[str] = ..., multisend_base: _Optional[str] = ..., multisend_delta: _Optional[str] = ..., edit_candidate: _Optional[str] = ..., set_halt_block: _Optional[str] = ..., edit_ticker_owner: _Optional[str] = ..., edit_multisig: _Optional[str] = ..., edit_candidate_public_key: _Optional[str] = ..., create_swap_pool: _Optional[str] = ..., add_liquidity: _Optional[str] = ..., remove_liquidity: _Optional[str] = ..., edit_candidate_commission: _Optional[str] = ..., mint_token: _Optional[str] = ..., burn_token: _Optional[str] = ..., vote_commission: _Optional[str] = ..., vote_update: _Optional[str] = ..., failed_tx: _Optional[str] = ..., add_limit_order: _Optional[str] = ..., remove_limit_order: _Optional[str] = ..., move_stake: _Optional[str] = ..., lock_stake: _Optional[str] = ..., lock: _Optional[str] = ...) -> None: ...

class OrderExpiredEvent(_message.Message):
    __slots__ = ("id", "address", "coin", "amount")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    address: str
    coin: int
    amount: str
    def __init__(self, id: _Optional[int] = ..., address: _Optional[str] = ..., coin: _Optional[int] = ..., amount: _Optional[str] = ...) -> None: ...

class UpdatedBlockRewardEvent(_message.Message):
    __slots__ = ("value", "value_locked_stake_rewards")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_LOCKED_STAKE_REWARDS_FIELD_NUMBER: _ClassVar[int]
    value: str
    value_locked_stake_rewards: str
    def __init__(self, value: _Optional[str] = ..., value_locked_stake_rewards: _Optional[str] = ...) -> None: ...

class StakeMoveEvent(_message.Message):
    __slots__ = ("address", "amount", "coin", "candidate_pub_key", "to_candidate_pub_key")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    TO_CANDIDATE_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    coin: int
    candidate_pub_key: str
    to_candidate_pub_key: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., coin: _Optional[int] = ..., candidate_pub_key: _Optional[str] = ..., to_candidate_pub_key: _Optional[str] = ...) -> None: ...

class UnlockEvent(_message.Message):
    __slots__ = ("address", "amount", "coin")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COIN_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    coin: int
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., coin: _Optional[int] = ...) -> None: ...
