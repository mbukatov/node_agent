from tendrl.commons import etcdobj
from tendrl.commons.message import Message as message
from tendrl.commons import objects


class Message(objects.BaseObject, message):
    internal = True
    def __init__(self, **message_arg):
        self._defs = {}
        message.__init__(self, **message_arg)
        objects.BaseObject.__init__(self)
        self.value = 'messages/events/%s'
        self._etcd_cls = _MessageEtcd
    
    def save(self):
        super(Message, self).save(update=False)
        
class _MessageEtcd(etcdobj.EtcdObj):
    """Message object, lazily updated

    """
    __name__ = 'messages/events/%s'
    _tendrl_cls = Message

    def render(self):
        self.__name__ = self.__name__ % (
            self.message_id
        )
        return super(_MessageEtcd, self).render()
