# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

import db

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)



class Select(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        pass
    __swig_destroy__ = None

    def addSelectable(self, selectable):
        return None

    def removeSelectable(self, selectable):
        return None

    def addSelectables(self, selectables):
        return None
    OBJECT = None
    ERROR = None
    TIMEOUT = None
    SIGNALINT = None

    def select(self, timeout=-1, interrupt_on_signal=False):
        return None

    def isQueueEmpty(self):
        return None

    @staticmethod
    def resultToString(result):
        return None


class FieldValuePairs(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return None
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return None

    def __bool__(self):
        return None

    def __len__(self):
        return None

    def __getslice__(self, i, j):
        return None

    def __setslice__(self, *args):
        return None

    def __delslice__(self, i, j):
        return None

    def __delitem__(self, *args):
        return None

    def __getitem__(self, *args):
        return None

    def __setitem__(self, *args):
        return None

    def pop(self):
        return None

    def append(self, x):
        return None

    def empty(self):
        return None

    def size(self):
        return None

    def swap(self, v):
        return None

    def begin(self):
        return None

    def end(self):
        return None

    def rbegin(self):
        return None

    def rend(self):
        return None

    def clear(self):
        return None

    def get_allocator(self):
        return None

    def pop_back(self):
        return None

    def erase(self, *args):
        return None

    def __init__(self, *args):
        pass

    def push_back(self, x):
        return None

    def front(self):
        return None

    def back(self):
        return None

    def assign(self, n, x):
        return None

    def resize(self, *args):
        return None

    def insert(self, *args):
        return None

    def reserve(self, n):
        return None

    def capacity(self):
        return None
    __swig_destroy__ = None

# Register FieldValuePairs in None
pass

class Selectable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = None

    def getFd(self):
        return None

    def readData(self):
        return None

    def hasData(self):
        return None

    def hasCachedData(self):
        return None

    def initializedWithData(self):
        return None

    def updateAfterRead(self):
        return None

    def getPri(self):
        return None
class RedisTransactioner(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, db):
        pass
    __swig_destroy__ = None

    def multi(self):
        return None

    def _exec(self):
        return None

    def enqueue(self, *args):
        return None

    def dequeueReply(self):
        return None

class TableBase(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        pass

    def getTableName(self):
        return None

    def getKeyName(self, key):
        return None

    def getTableNameSeparator(self):
        return None

    def getChannelName(self, *args):
        return None
    __swig_destroy__ = None


class TableEntryPoppable(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = None

    def pop(self, *args, **kwargs):
        return None

    def pops(self, *args, **kwargs):
        return None

class RedisSelect(Selectable):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SUBSCRIBE_TIMEOUT = None

    def __init__(self, pri=0):
        pass

    def getFd(self):
        return None

    def readData(self):
        return None

    def hasData(self):
        return None

    def hasCachedData(self):
        return None

    def initializedWithData(self):
        return None

    def updateAfterRead(self):
        return None

    def getDbConnector(self):
        return None

    def subscribe(self, db, channelName):
        return None

    def psubscribe(self, db, channelName):
        return None

    def punsubscribe(self, channelName):
        return None

    def setQueueLength(self, queueLength):
        return None
    __swig_destroy__ = None

class TableConsumable(TableBase, TableEntryPoppable, RedisSelect):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    DEFAULT_POP_BATCH_SIZE = None
    __swig_destroy__ = None

class ConsumerTableBase(TableConsumable, RedisTransactioner):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    POP_BATCH_SIZE = property(None)
    __swig_destroy__ = None

    def getDbConnector(self):
        return None

    def pop(self, *args):
        return None

    def empty(self):
        return None



class SubscriberStateTable(ConsumerTableBase):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        pass

    def readData(self):
        return None

    def hasData(self):
        return None

    def hasCachedData(self):
        return None

    def initializedWithData(self):
        return None
    __swig_destroy__ = None




def CastSelectableToRedisSelectObj(temp):
    return None



class FieldValueMap(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return None
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return None

    def __bool__(self):
        return None

    def __len__(self):
        return None
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return None

    def __delitem__(self, key):
        return None

    def has_key(self, key):
        return None

    def keys(self):
        return None

    def values(self):
        return None

    def items(self):
        return None

    def __contains__(self, key):
        return None

    def key_iterator(self):
        return None

    def value_iterator(self):
        return None

    def __setitem__(self, *args):
        return None

    def asdict(self):
        return None

    def __init__(self, *args):
        pass

    def empty(self):
        return None

    def size(self):
        return None

    def swap(self, v):
        return None

    def begin(self):
        return None

    def end(self):
        return None

    def rbegin(self):
        return None

    def rend(self):
        return None

    def clear(self):
        return None

    def get_allocator(self):
        return None

    def count(self, x):
        return None

    def erase(self, *args):
        return None

    def find(self, x):
        return None

    def lower_bound(self, x):
        return None

    def upper_bound(self, x):
        return None
    __swig_destroy__ = None




def events_init_publisher(event_source):
    return None

def events_deinit_publisher(handle):
    return None

EVENT_TS_PARAM = None
EVENT_MAXSZ = None

def event_publish(handle, event_tag, params=None):
    return None


class RedisContext(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DEFAULT_UNIXSOCKET = None

    def __init__(self, other):
        pass
    __swig_destroy__ = None

    def getContext(self):
        return None

    def setClientName(self, clientName):
        return None

    def getClientName(self):
        return None

class DBConnector(RedisContext):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DEFAULT_UNIXSOCKET = None

    def __init__(self, *args):
        pass

    def getDbId(self):
        return None

    def getDbName(self):
        return None

    def getNamespace(self):
        return None

    namespace = property(getNamespace)


    @staticmethod
    def select(db):
        return None

    def newConnector(self, timeout):
        return None

    def pubsub(self):
        return None

    def _del(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


    def exists(self, key):
        return None

    def hdel(self, *args):
        return None

    def delete(self, *args):
        return None

    def keys(self, key):
        return None

    def scan(self, *args, **kwargs):
        return None

    def set(self, *args):
        return None

    def hset(self, key, field, value):
        return None

    def hmset(self, multiHash):
        return None

    def get(self, key):
        return None

    def hget(self, key, field):
        return None

    def hexists(self, key, field):
        return None

    def incr(self, key):
        return None

    def decr(self, key):
        return None

    def rpush(self, list, item):
        return None

    def blpop(self, list, timeout):
        return None

    def subscribe(self, pattern):
        return None

    def psubscribe(self, pattern):
        return None

    def punsubscribe(self, pattern):
        return None

    def publish(self, channel, message):
        return None

    def config_set(self, key, value):
        return None

    def flushdb(self):
        return None

    def hgetall(self, key):
        return None
    __swig_destroy__ = None


class SonicDBConfig(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DEFAULT_SONIC_DB_CONFIG_FILE = None
    DEFAULT_SONIC_DB_GLOBAL_CONFIG_FILE = None

    @staticmethod
    def initialize(*args, **kwargs):
        return None

            ## TODO: the python function and C++ one is not on-par
    @staticmethod
    def load_sonic_db_config(sonic_db_file_path=DEFAULT_SONIC_DB_CONFIG_FILE):
        SonicDBConfig.initialize(sonic_db_file_path)


    @staticmethod
    def initializeGlobalConfig(*args, **kwargs):
        return None

            ## TODO: the python function and C++ one is not on-par
    @staticmethod
    def load_sonic_global_db_config(global_db_file_path=DEFAULT_SONIC_DB_GLOBAL_CONFIG_FILE, namespace=None):
        SonicDBConfig.initializeGlobalConfig(global_db_file_path)


    @staticmethod
    def validateNamespace(netns):
        return None

    @staticmethod
    def getDbInst(*args, **kwargs):
        return None

    @staticmethod
    def getDbId(*args, **kwargs):
        return None

    @staticmethod
    def getSeparator(*args):
        return None

    @staticmethod
    def getDbSock(*args, **kwargs):
        return None

    @staticmethod
    def getDbHostname(*args, **kwargs):
        return None

    @staticmethod
    def getDbPort(*args, **kwargs):
        return None

    @staticmethod
    def getNamespaces():
        return None

            ## TODO: the python function and C++ one is not on-par
    @staticmethod
    def get_ns_list():
        return SonicDBConfig.getNamespaces()


    @staticmethod
    def getDbList(*args, **kwargs):
        return None

    @staticmethod
    def isInit():
        return None

    @staticmethod
    def isGlobalInit():
        return None

    @staticmethod
    def getInstanceList(*args, **kwargs):
        return None

    def __init__(self):
        pass
    __swig_destroy__ = None


class SonicV2Connector_Native(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SonicV2Connector_Native, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SonicV2Connector_Native, name)
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        self.client = db.DBClient()

    def getNamespace(self):
        return None

    def connect(self, db_name, retry_on=True):
        return self.client.connect(db_name)

    def close(self, db_name):
        return self.client.close(db_name)

    def get_db_list(self):
        return ('STATE_DB', 'APPL_DB', 'GB_FLEX_COUNTER_DB', 'APPL_STATE_DB', 'ASIC_DB', 'CONFIG_DB', 'COUNTERS_DB', 'LOGLEVEL_DB', 'GB_ASIC_DB', 'GB_COUNTERS_DB', 'PFC_WD_DB', 'FLEX_COUNTER_DB', 'RESTAPI_DB', 'SNMP_OVERLAY_DB')

    def get_dbid(self, db_name):
        return None

    def get_db_separator(self, db_name):
        return None

    def get_redis_client(self, db_name):
        return None

    def publish(self, db_name, channel, message):
        return None

    def exists(self, db_name, key):
        return None

    def keys(self, *args, **kwargs):
        return self.client.raw_to_list(self.client.keys(*args))

    def scan(self, *args, **kwargs):
        return None

    def get(self, db_name, _hash, key, blocking=False):
        return None

    def hexists(self, db_name, _hash, key):
        return None

    def get_all(self, db_name, _hash, blocking=False):
        return {}

    def hmset(self, db_name, key, values):
        return None

    def set(self, db_name, _hash, key, val, blocking=False):
        return None

    def delete(self, db_name, key, blocking=False):
        return None

    def delete_all_by_pattern(self, db_name, pattern):
        return None
    __swig_destroy__ = None



class SonicV2Connector(SonicV2Connector_Native):
## Note: there is no easy way for SWIG to map ctor parameter netns(C++) to namespace(python)
    def __init__(self, use_unix_socket_path = False, namespace = '', **kwargs):
        if 'host' in kwargs:
# Note: host argument will be ignored, same as in sonic-py-swsssdk
            kwargs.pop('host')
        if 'decode_responses' in kwargs and kwargs.pop('decode_responses') != True:
            raise ValueError('decode_responses must be True if specified, False is not supported')
        if namespace is None:
            namespace = ''
        super(SonicV2Connector, self).__init__(use_unix_socket_path = use_unix_socket_path, netns = namespace)

# Add database name attributes into SonicV2Connector instance
# Note: this is difficult to implement in C++
        for db_name in self.get_db_list():
# set a database name as a constant value attribute.
            setattr(self, db_name, db_name)

    @property
    def namespace(self):
        return self.getNamespace()

    def get_all(self, db_name, _hash, blocking=False):
        return dict(super(SonicV2Connector, self).get_all(db_name, _hash, blocking))

    def keys(self, *args, **kwargs):
        return list(super(SonicV2Connector, self).keys(*args, **kwargs))

    def set(self, db_name, _hash, key, value, blocking=False):
        if isinstance(value, str):
            return super(SonicV2Connector, self).set(db_name, _hash, key, value, blocking)

        return super(SonicV2Connector, self).set(db_name, _hash, key, str(value), blocking)



class ConfigDBConnector_Native(SonicV2Connector_Native):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    INIT_INDICATOR = None

    def __init__(self, *args, **kwargs):
        super(ConfigDBConnector_Native, self).__init__(args, kwargs)
        pass

    def db_connect(self, db_name, wait_for_init=False, retry_on=False):
        return self.client.connect(db_name)

    def connect(self, wait_for_init=True, retry_on=False):
        return None

    def set_entry(self, table, key, data):
        return self.client.hset(table, key, data)

    def mod_entry(self, table, key, data):
        return self.client.hset(table, key, data)

    def get_entry(self, table, key):
        return self.client.hget(table, key)

    def get_keys(self, table, split=True):
        return self.client.keys(table)

    def get_table(self, table):
        return self.client.get_table(table)

    def delete_table(self, table):
        return None

    def mod_config(self, data):
        return None

    def get_config(self):
        return None

    def getKeySeparator(self):
        return None

    def getTableNameSeparator(self):
        return None

    def getDbName(self):
        return None
    __swig_destroy__ = None



class ConfigDBConnector(SonicV2Connector, ConfigDBConnector_Native):

## Note: there is no easy way for SWIG to map ctor parameter netns(C++) to namespace(python)
    def __init__(self, use_unix_socket_path = False, namespace = '', **kwargs):
        if 'decode_responses' in kwargs and kwargs.pop('decode_responses') != True:
            raise ValueError('decode_responses must be True if specified, False is not supported')
        if namespace is None:
            namespace = ''
        super(ConfigDBConnector, self).__init__(use_unix_socket_path = use_unix_socket_path, namespace = namespace)

# Trick: to achieve static/instance method "overload", we must use initize the function in ctor
# ref: https://stackoverflow.com/a/28766809/2514803
        self.serialize_key = self._serialize_key
        self.deserialize_key = self._deserialize_key

## Note: callback is difficult to implement by SWIG C++, so keep in python
        self.handlers = {}
        self.fire_init_data = {}

    @property
    def KEY_SEPARATOR(self):
        return self.getKeySeparator()

    @property
    def TABLE_NAME_SEPARATOR(self):
        return self.getTableNameSeparator()

    @property
    def db_name(self):
        return self.getDbName()

## Note: callback is difficult to implement by SWIG C++, so keep in python
    def listen(self, init_data_handler=None):
## Start listen Redis keyspace event. Pass a callback function to `init` to handle initial table data.
        self.pubsub = self.get_redis_client(self.db_name).pubsub()
        self.pubsub.psubscribe("__keyspace@{}__:*".format(self.get_dbid(self.db_name)))

# Build a cache of data for all subscribed tables that will recieve the initial table data so we dont send duplicate event notifications
        init_data = {tbl: self.get_table(tbl) for tbl in self.handlers if init_data_handler or self.fire_init_data[tbl]}

# Function to send initial data as series of updates through individual table callback handlers
        def load_data(tbl, data):
            if self.fire_init_data[tbl]:
                for row, x in data.items():
                    self.__fire(tbl, row, x)
                return False
            return True

        init_callback_data = {tbl: data for tbl, data in init_data.items() if load_data(tbl, data)}

# Pass all initial data that we DID NOT send as updates to handlers through the init callback if provided by caller
        if init_data_handler:
            init_data_handler(init_callback_data)

        while True:
            item = self.pubsub.listen_message(interrupt_on_signal=True)
            if 'type' not in item:
# When timeout or interrupted, item will not contains 'type'
                continue

            if item['type'] == 'pmessage':
                key = item['channel'].split(':', 1)[1]
                try:
                    (table, row) = key.split(self.TABLE_NAME_SEPARATOR, 1)
                    if table in self.handlers:
                        client = self.get_redis_client(self.db_name)
                        data = self.raw_to_typed(client.hgetall(key))
                        if table in init_data and row in init_data[table]:
                            cache_hit = init_data[table][row] == data
                            del init_data[table][row]
                            if not init_data[table]:
                                del init_data[table]
                            if cache_hit: continue
                        self.__fire(table, row, data)
                except ValueError:
                    pass    #Ignore non table-formated redis entries

## Dynamic typed functions used in python
    @staticmethod
    def raw_to_typed(raw_data):
        if raw_data is None:
            return None
        typed_data = {}

        for raw_key in raw_data:
            key = raw_key
# "NULL:NULL" is used as a placeholder for objects with no attributes
            if key == "NULL":
                pass
# A column key with ending '@' is used to mark list-typed table items
# TODO: Replace this with a schema-based typing mechanism.
            elif key.endswith("@"):
                value = raw_data[raw_key].split(',')
                typed_data[key[:-1]] = value
            else:
                typed_data[key] = raw_data[raw_key]
        return typed_data

    @staticmethod
    def typed_to_raw(typed_data):
        if typed_data is None:
            return {}
        elif len(typed_data) == 0:
            return { "NULL": "NULL" }
        raw_data = {}
        for key in typed_data:
            value = typed_data[key]
            if type(value) is list:
                raw_data[key+'@'] = ','.join(value)
            else:
                raw_data[key] = str(value)
        return raw_data

# Note: we could not use a class variable for KEY_SEPARATOR, but original dependent code is using
# these static functions. So we implement both static and instance functions with the same name.
# The static function will behave according to ConfigDB separators.
    @staticmethod
    def serialize_key(key, separator='|'):
        if type(key) is tuple:
            return separator.join(key)
        else:
            return str(key)

    def _serialize_key(self, key):
        return ConfigDBConnector.serialize_key(key, self.KEY_SEPARATOR)

    @staticmethod
    def deserialize_key(key, separator='|'):
        tokens = key.split(separator)
        if len(tokens) > 1:
            return tuple(tokens)
        else:
            return key

    def _deserialize_key(self, key):
        return ConfigDBConnector.deserialize_key(key, self.KEY_SEPARATOR)

    def __fire(self, table, key, data):
        if table in self.handlers:
            handler = self.handlers[table]
            handler(table, key, data)

    def subscribe(self, table, handler, fire_init_data=False):
        self.handlers[table] = handler
        self.fire_init_data[table] = fire_init_data

    def unsubscribe(self, table):
        if table in self.handlers:
            self.handlers.pop(table)

    def set_entry(self, table, key, data):
        key = self.serialize_key(key)
        raw_data = self.typed_to_raw(data)
        super(ConfigDBConnector, self).set_entry(table, key, raw_data)

    def mod_config(self, data):
        raw_config = {}
        try:
            for table_name, table_data in data.items():
                raw_config[table_name] = {}
                if table_data == None:
                    continue
                for key, data in table_data.items():
                    raw_key = self.serialize_key(key)
                    raw_data = self.typed_to_raw(data)
                    raw_config[table_name][raw_key] = raw_data
        except:
            pass
        super(ConfigDBConnector, self).mod_config(raw_config)

    def mod_entry(self, table, key, data):
        key = self.serialize_key(key)
        raw_data = self.typed_to_raw(data)
        super(ConfigDBConnector, self).mod_entry(table, key, raw_data)

    def get_entry(self, table, key):
        key = self.serialize_key(key)
        raw_data = super(ConfigDBConnector, self).get_entry(table, key)
        return self.raw_to_typed(raw_data)

    def get_keys(self, table, split=True):
        keys = super(ConfigDBConnector, self).get_keys(table, split)
        ret = []
        for key in keys:
            ret.append(self.deserialize_key(key))
        return ret

    def get_table(self, table):
        data = super(ConfigDBConnector, self).get_table(table)
        ret = {}
        try:
            for row, entry in data.items():
                entry = self.raw_to_typed(entry)
                ret[self.deserialize_key(row)] = entry
        except:
            pass
        return ret

    def get_config(self):
        data = super(ConfigDBConnector, self).get_config()
        ret = {}
        try:
            for table_name, table in data.items():
                for row, entry in table.items():
                    entry = self.raw_to_typed(entry)
                    ret.setdefault(table_name, {})[self.deserialize_key(row)] = entry
        except:
            pass
        return ret

class ConfigDBPipeConnector_Native(ConfigDBConnector_Native):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        super(ConfigDBPipeConnector_Native, self).__init__(args, kwargs)

    def set_entry(self, table, key, data):
        return None

    def mod_config(self, data):
        return None

    def get_config(self):
        return None
    __swig_destroy__ = None

class ConfigDBPipeConnector(ConfigDBConnector, ConfigDBPipeConnector_Native):

## Note: diamond inheritance, reusing functions in both classes
    def __init__(self, **kwargs):
        super(ConfigDBPipeConnector, self).__init__(**kwargs)

class TableBase(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        pass

    def getTableName(self):
        return None

    def getKeyName(self, key):
        return None

    def getTableNameSeparator(self):
        return None

    def getChannelName(self, *args):
        return None
    __swig_destroy__ = None
