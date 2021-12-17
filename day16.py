import math

from common import read_input_lines


def _parse_header(binary: str) -> tuple[int, int, str]:
    version = binary[:3]
    type_id = binary[3:6]
    return (int(version, 2), int(type_id, 2), binary[6:])


def _parse_literal_value(binary: str) -> tuple[int, str]:
    literal_value_arr: list[str] = []
    while True:
        if binary[0] == "0":
            literal_value_arr.append(binary[1:5])
            binary = binary[5:]
            break
        literal_value_arr.append(binary[1:5])
        binary = binary[5:]
    literal_value = "".join(literal_value_arr)
    return (int(literal_value, 2), binary)


def _parse_length_type_id(binary: str) -> tuple[int, str]:
    return (int(binary[0], 2), binary[1:])


def _parse_total_length_in_bits(binary: str) -> tuple[int, str]:
    return (int(binary[:15], 2), binary[15:])


def _parse_number_of_contained_packages(binary: str) -> tuple[int, str]:
    return (int(binary[:11], 2), binary[11:])


class Packet:
    sub_packets: list["Packet"]

    def __init__(self, binary: str):
        self.sub_packets = []
        self.original_binary = binary
        self.version, self.type_id, self.binary = _parse_header(binary)

        if self.type_id == 4:
            self.value, self.binary = _parse_literal_value(self.binary)
        else:
            length_type_id, self.binary = _parse_length_type_id(self.binary)

            if length_type_id == 0:
                total_length, self.binary = _parse_total_length_in_bits(self.binary)
                sub_binary = self.binary[:total_length]
                self.binary = self.binary[total_length:]

                while True:
                    sub_packet = Packet(sub_binary)
                    sub_binary = sub_packet.binary
                    self.sub_packets.append(sub_packet)

                    if not len(sub_binary.strip()):
                        break
            else:
                sub_packet_count, self.binary = _parse_number_of_contained_packages(
                    self.binary
                )

                for _ in range(sub_packet_count):
                    sub_packet = Packet(self.binary)
                    self.sub_packets.append(sub_packet)
                    self.binary = sub_packet.binary

    def add_version_numbers(self) -> int:
        return self.version + sum([p.add_version_numbers() for p in self.sub_packets])

    def eval(self) -> int:
        if self.type_id == 0:
            return sum([p.eval() for p in self.sub_packets])
        elif self.type_id == 1:
            return math.prod([p.eval() for p in self.sub_packets])
        elif self.type_id == 2:
            return min([p.eval() for p in self.sub_packets])
        elif self.type_id == 3:
            return max([p.eval() for p in self.sub_packets])
        elif self.type_id == 4:
            return self.value
        elif self.type_id == 5:
            [a, b] = self.sub_packets
            return 1 if a.eval() > b.eval() else 0
        elif self.type_id == 6:
            [a, b] = self.sub_packets
            return 1 if a.eval() < b.eval() else 0
        elif self.type_id == 7:
            [a, b] = self.sub_packets
            return 1 if a.eval() == b.eval() else 0
        return -1


def part1(input: list[str]) -> int:
    binary = bin(int("".join(input), 16))[2:]
    missing_zeros = 4 - len(binary) % 4
    binary = "0" * (0 if missing_zeros == 4 else missing_zeros) + binary
    p = Packet(binary)
    return p.add_version_numbers()


def part2(input: list[str]) -> int:
    binary = bin(int("".join(input), 16))[2:]
    missing_zeros = 4 - len(binary) % 4
    binary = "0" * (0 if missing_zeros == 4 else missing_zeros) + binary
    p = Packet(binary)
    return p.eval()


def parse(*, example: bool = False) -> list[str]:
    return [c for c in read_input_lines(16, str, example=example)[0]]


if __name__ == "__main__":
    data_in = parse()
    print(part1(data_in))
    print(part2(data_in))
