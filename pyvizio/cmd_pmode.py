from .protocol import get_json_obj, ProtoConstants, InfoCommandBase, CommandBase, Endpoints


class VizioPmode(object):
    def __init__(self, json_item, is_extended_metadata):
        self.id = int(get_json_obj(json_item, ProtoConstants.Item.HASHVAL))
        self.c_name = get_json_obj(json_item, ProtoConstants.Item.CNAME)
        self.type = get_json_obj(json_item, ProtoConstants.Item.TYPE)
        self.name = get_json_obj(json_item, ProtoConstants.Item.NAME)
        self.meta_name = None
        self.meta_data = None

        meta = get_json_obj(json_item, ProtoConstants.Item.VALUE)
        if meta is not None:
            if is_extended_metadata:
                self.meta_name = get_json_obj(meta, ProtoConstants.Item.NAME)
                self.meta_data = get_json_obj(meta, ProtoConstants.Item.METADATA)
            else:
                self.meta_name = meta

        if self.meta_name is None or "" == self.meta_name:
            self.meta_name = self.c_name


class GetPmodesListCommand(InfoCommandBase):
    """Obtaining list of available picture modes"""

    def __init__(self, device_type):
        super(GetPmodesListCommand, self).__init__()
        InfoCommandBase.url.fset(self, Endpoints.ENDPOINTS[device_type]["PMODES"])
        self._device_type = device_type

    def process_response(self, json_obj):
        items = get_json_obj(json_obj, ProtoConstants.RESPONSE_ITEMS)
        
        # Last input for sound bar is the current input so it needs to be removed before processing
#        if self._device_type == "soundbar":
#            items = items[:-1]

        pmodes = []

        if items is not None:
            for itm in items:
                v_pmode = VizioPmode(itm, True)
                pmodes.append(v_pmode)

        return pmodes


class GetCurrentPmodeCommand(InfoCommandBase):
    """Obtaining current picture mode"""

    def __init__(self, device_type):
        super(GetCurrentPmodeCommand, self).__init__()
        InfoCommandBase.url.fset(self, Endpoints.ENDPOINTS[device_type]["CURR_PMODE"])

    def process_response(self, json_obj):
        items = get_json_obj(json_obj, ProtoConstants.RESPONSE_ITEMS)
        v_pmode = None
        if len(items) > 0:
            v_pmode = VizioPmode(items[0], False)
        return v_pmode


class ChangePmodeCommand(CommandBase):
    def __init__(self, id_, name, device_type):
        super(ChangePmodeCommand, self).__init__()
        CommandBase.url.fset(self, Endpoints.ENDPOINTS[device_type]["SET_PMODE"])
        self.VALUE = str(name)
        # noinspection SpellCheckingInspection
        self.HASHVAL = int(id_)
        self.REQUEST = ProtoConstants.ACTION_MODIFY

    def process_response(self, json_obj):
        return True
