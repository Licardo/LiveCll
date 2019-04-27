

class Utils(object):

    @staticmethod
    def filter_content(content, keys):
        for key in keys:
            if content.find(key) != -1:
                return True
        return False
