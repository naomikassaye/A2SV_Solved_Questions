from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}

        for p in paths:
            parts = p.split(' ')
            dir_path = parts[0]

            for f in parts[1:]:
                name_chars = []
                content_chars = []
                inside = False

                for c in f:
                    if c == '(':
                        inside = True
                    elif c == ')':
                        inside = False
                        break
                    elif inside:
                        content_chars.append(c)
                    else:
                        name_chars.append(c)

                name = ''.join(name_chars)
                content = ''.join(content_chars)
                files.setdefault(content, []).append(dir_path + '/' + name)

        return [lst for lst in files.values() if len(lst) > 1]