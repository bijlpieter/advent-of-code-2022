from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import count


def scorify(iterable):
    return dict(zip(iterable, count(1)))


CARD_SCORING: dict[int, dict[str, int]] = {
    1: scorify("23456789TJQKA"),
    2: scorify("J23456789TQKA"),
}
HAND_SCORING: dict[tuple, int] = scorify(
    [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]
)


@dataclass
class Hand:
    hand: str
    bid: int

    def card_counts(self, part=1) -> tuple[int, ...]:
        counter = Counter(self.hand)
        if part == 2:
            jokers = counter.pop("J", 0)
            top = counter.most_common(n=1)
            best = top[0][0] if top else "J"
            counter.update({best: jokers})
        return tuple(sorted(counter.values()))

    def hand_score(self, part=1) -> int:
        return HAND_SCORING[self.card_counts(part)]

    def card_scores(self, part=1) -> tuple[int, ...]:
        return tuple(map(CARD_SCORING[part].__getitem__, self.hand))

    def order(self, part=1) -> tuple[int, ...]:
        return (self.hand_score(part), *self.card_scores(part))

    @staticmethod
    def from_line(line: str) -> Hand:
        hand, bid = line.split()
        return Hand(hand=hand, bid=int(bid))


@dataclass
class CamelCards:
    hands: list[Hand]

    @staticmethod
    def from_text(text: str) -> CamelCards:
        return CamelCards(list(map(Hand.from_line, text.split("\n"))))

    def winnings(self, part=1) -> int:
        sorted_hands = sorted(self.hands, key=lambda h: h.order(part))
        return sum(rank * hand.bid for rank, hand in enumerate(sorted_hands, start=1))


with open("day07.txt") as fp:
    file = fp.read().strip()

game = CamelCards.from_text(file)
print(game.winnings(part=1))
print(game.winnings(part=2))
