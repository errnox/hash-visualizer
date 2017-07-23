import os

DEFAULT_VISUALIZATION_TYPE = 'shell'

class Visualizer(object):
    def __init__(self, vis_type=DEFAULT_VISUALIZATION_TYPE):
        self.DEFAULT_VISUALIZATION_TYPE = vis_type

        self._symbols = {
            '0': 1,
            '1': 2,
            '2': 3,
            '3': 4,
            '4': 5,
            '5': 6,
            '6': 7,
            '7': 8,
            '8': 9,
            '9': 10,
            'a': 11,
            'b': 12,
            'c': 13,
            'd': 14,
            'e': 15,
            'f': 16
            }

        self._symbols_exptension = {
            'g': 17,
            'h': 18,
            'i': 19,
            'j': 20,
            'k': 21,
            'l': 22,
            'm': 23,
            'n': 24,
            'o': 25,
            'p': 26,
            'q': 27,
            'r': 28,
            's': 29,
            't': 30,
            'u': 31,
            'v': 32,
            'w': 33,
            'x': 34,
            'y': 35,
            'z': 36
            }

        self._hexcolors = {
            "0": ["#0000FF", "Blue"],
            "1": ["#8A2BE2", "BlueViolet"],
            "2": ["#A52A2A", "Brown"],
            "3": ["#DEB887", "BurlyWood"],
            "4": ["#5F9EA0", "CadetBlue"],
            "5": ["#7FFF00", "Chartreuse"],
            "6": ["#D2691E", "Chocolate"],
            "7": ["#FF7F50", "Coral"],
            "8": ["#6495ED", "CornflowerBlue"],
            "9": ["#FFF8DC", "Cornsilk"],
            "a": ["#DC143C", "Crimson"],
            "b": ["#00FFFF", "Cyan"],
            "c": ["#00008B", "DarkBlue"],
            "d": ["#008B8B", "DarkCyan"],
            "e": ["#B8860B", "DarkGoldenRod"],
            "f": ["#A9A9A9", "DarkGray"]
            }

        self._colormap_extension = {
            "g": ["#A9A9A9", "DarkGrey"],
            "h": ["#006400", "DarkGreen"],
            "i": ["#BDB76B", "DarkKhaki"],
            "j": ["#8B008B", "DarkMagenta"],
            "k": ["#556B2F", "DarkOliveGreen"],
            "l": ["#FF8C00", "Darkorange"],
            "m": ["#9932CC", "DarkOrchid"],
            "n": ["#8B0000", "DarkRed"],
            "o": ["#E9967A", "DarkSalmon"],
            "p": ["#8FBC8F", "DarkSeaGreen"],
            "q": ["#483D8B", "DarkSlateBlue"],
            "r": ["#2F4F4F", "DarkSlateGray"],
            "s": ["#2F4F4F", "DarkSlateGrey"],
            "t": ["#00CED1", "DarkTurquoise"],
            "u": ["#9400D3", "DarkViolet"],
            "v": ["#FF1493", "DeepPink"],
            "w": ["#00BFFF", "DeepSkyBlue"],
            "x": ["#696969", "DimGray"],
            "y": ["#696969", "DimGrey"],
            "z": ["#1E90FF", "DodgerBlue"]
            }

        self._shell_escape_sequences_fg = {
            "0": ["0;30", "Black"],
            "1": ["0;34", "Blue"],
            "2": ["0;32", "Green"],
            "3": ["0;36", "Cyan"],
            "4": ["0;31", "Red"],
            "5": ["0;35", "Purple"],
            "6": ["0;33", "Brown"],
            "7": ["0;37", "Light Gray"],
            "8": ["1;30", "Dark Gray"],
            "9": ["1;34", "Light Blue"],
            "a": ["1;32", "Light Green"],
            "b": ["1;36", "Light Cyan"],
            "c": ["1;31", "Light Red"],
            "d": ["1;35", "Light Purple"],
            "e": ["1;33", "Yellow"],
            "f": ["1;37", "White"]
            }

        self._shell_escape_sequences_bg_X = {
            "0": ["0;40", "Black"],
            "1": ["0;44", "Blue"],
            "2": ["0;42", "Green"],
            "3": ["0;46", "Cyan"],
            "4": ["0;41", "Red"],
            "5": ["0;45", "Purple"],
            "6": ["0;43", "Brown"],
            "7": ["0;47", "Light Gray"],
            "8": ["1;40", "Dark Gray"],
            "9": ["1;44", "Light Blue"],
            "a": ["1;42", "Light Green"],
            "b": ["1;46", "Light Cyan"],
            "c": ["1;41", "Light Red"],
            "d": ["1;45", "Light Purple"],
            "e": ["1;43", "Yellow"],
            "f": ["1;47", "White"]
            }

        self._shell_escape_sequences_bg = {
            "0": ["0;40", "Black"],
            "1": ["0;41", "Red"],
            "2": ["0;42", "Green"],
            "3": ["0;43", "Brown"],
            "4": ["0;44", "Blue"],
            "5": ["0;45", "Purple"],
            "6": ["0;46", "Cyan"],
            "7": ["0;47", "Light Gray"],
            "8": ["0;30", "Dark Gray"],
            "9": ["0;31", "Light Red"],
            "a": ["0;32", "Light Green"],
            "b": ["0;33", "Yellow"],
            "c": ["0;34", "Light Blue"],
            "d": ["0;35", "Light Purple"],
            "e": ["0;36", "Light Cyan"],
            "f": ["0;37", "White"],
            }

        self.colormap = self._shell_escape_sequences_bg

    def visualize_hash(self, hash,
                       type=DEFAULT_VISUALIZATION_TYPE):
        visualized_hash = ''

        if type == 'shell':
            visualized_hash = self._visualize_hash_shell(hash)
        else:
            pass  # TODO: HTML/PDF/PNG/JPEG/SVG/... output

        return visualized_hash

    def visualize_hashes(self, hashes,
                         type=DEFAULT_VISUALIZATION_TYPE):
        visualized_hashes = []
        for hash in hashes:
            visualized_hashes.append(self.visualize_hash(hash))
        return visualized_hashes

    def _visualize_hash_shell(self, hash):
        visualized_hash = ''

        hash = self._sort_hash(hash)

        for char in hash:
            visualized_hash += '\033[' + self.colormap[char][0] + 'mH'

        visualized_hash += '\033[m'
        return visualized_hash

    # Bubble sort
    def _sort_hash(self, hash):
        sorted_hash = [char for char in hash]

        tmp = ''

        max = len(sorted_hash)

        for n in range(max):
            for i in range(max - 1):
                tmp = sorted_hash[i]

                if self._symbols[sorted_hash[i]] > self._symbols[sorted_hash[i - 1]]:
                    sorted_hash[i] = sorted_hash[i - 1]
                    sorted_hash[i - 1] = tmp

        sorted_hash_string = ''

        for char in sorted_hash:
            sorted_hash_string += char

        return sorted_hash_string


if __name__ == '__main__':
    test_hashes = []
    with open(os.getcwd() + '/res/hashes/testhashes', 'r') as hashfile:
        test_hashes = [line.replace(os.linesep, '') for line in hashfile]

    visualizer = Visualizer()
    for hash in visualizer.visualize_hashes(test_hashes):
        print hash
