class Solution:

    def encode(self, strings: List[str]) -> str:
        encoded_parts = []

        for word in strings:
            encoded_parts.append(str(len(word)))
            encoded_parts.append("#")
            encoded_parts.append(word)

        return "".join(encoded_parts)

    def decode(self, encoded_string: str) -> List[str]:
        decoded_strings = []
        index = 0

        while index < len(encoded_string):
            delimiter_index = index

            while encoded_string[delimiter_index] != "#":
                delimiter_index += 1

            word_length = int(encoded_string[index:delimiter_index])

            start = delimiter_index + 1
            end = start + word_length

            decoded_strings.append(encoded_string[start:end])

            index = end

        return decoded_strings