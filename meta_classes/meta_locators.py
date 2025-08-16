
class MetaLocator(type):

    def __new__(cls, name, bases, attrs):
        # Iterate over all attributes passed to the class
        for key, value in attrs.items():
            if isinstance(value, str):

                if value.startswith('//') or value.startswith('.//') or value.startswith('(//'):
                    # Transform string into XPath locator if it starts with '//' or './/'
                    attrs[key] = ('xpath', value)

                elif value.startswith('.') or value.startswith('#') or value.startswith('['):
                    # # Transform string into CSS selector locator if it starts with '.' or '#' or '['
                    attrs[key] = ('css selector', value)

        return type.__new__(cls, name, bases, attrs)