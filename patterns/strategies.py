from abc import ABC, abstractmethod
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, creatures:list[Creature]) -> list[Creature]: ...

class SortByPower(SortStrategy):
    def sort(self, creatures:list[Creature]) -> list[Creature]:
        return creatures.sort(key=lambda creature: creature.power, reverse=True)

class SortByName(SortStrategy):
    def sort(self, creatures:list[Creature]) -> list[Creature]:
        return creatures.sort(key=lambda creature: creature.name)

class SortByAvailability(SortStrategy):
    def sort(self, creatures:list[Creature]) -> list[Creature]:
        creatures_in_stable = []
        creature_in_mission = []
        for creature in creatures:
            if creature._in_stable:
                creatures_in_stable.append(creature)
            else:
                creature_in_mission.append(creature)
        fullList = []
        fullList.extend(SortByName.sort(creatures_in_stable))
        fullList.extend(SortByName.sort(creature_in_mission))
        return fullList