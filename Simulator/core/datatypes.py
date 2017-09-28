class NamedObjectList(list):
    def __getitem__(self, key):
        if isinstance(key, str):
            for item in self:
                if item.name == key:
                    return item
            raise IndexError('no object named {!r}'.format(key))
        return list.__getitem__(self, key)