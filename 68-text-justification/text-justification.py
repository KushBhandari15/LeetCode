class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        line = []
        num_of_letters = 0

        for word in words:
            # Check if adding the next word exceeds the line width
            if num_of_letters + len(word) + len(line) > maxWidth:
                if len(line) == 1:
                    res.append(line[0] + ' ' * (maxWidth - num_of_letters))
                else:
                    spaces = maxWidth - num_of_letters
                    space_between_words = spaces // (len(line) - 1)
                    extra_spaces = spaces % (len(line) - 1)

                    for i in range(extra_spaces):
                        line[i] += ' '

                    res.append((' ' * space_between_words).join(line))
                line = []
                num_of_letters = 0

            line.append(word)
            num_of_letters += len(word)

        # Handle the last line (left-justified)
        res.append(' '.join(line) + ' ' * (maxWidth - num_of_letters - (len(line) - 1)))

        return res
