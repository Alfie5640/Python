

def sort_ages(ages_list: list) -> list:
    aages_list = ages_list.copy()
    aages_list.sort()
    return aages_list


def avg_ages(ages_list: list) -> int:
    bages_list = ages_list.copy()
    bages_list = sum(bages_list) / (len(bages_list))
    bages_list = round(bages_list)
    return bages_list


def min_age(ages_list: list) -> int:
    cages_list = ages_list.copy()
    cages_list = min(cages_list)
    return cages_list


def max_age(ages_list: list) -> int:
    dages_list = ages_list.copy()
    dages_list = max(dages_list)
    return dages_list


def reverse_sort(ages_list: list) -> list:
    eages_list = ages_list.copy()
    eages_list.sort()
    eages_list.reverse()
    return eages_list

ages_list = [15, 38, 23, 91, 45, 40, 2, 51, 76, 31, 13, 10, 32, 76, 85]
print("The list of ages is " + str(ages_list))
print("The list in order is ")
print(sort_ages(ages_list))
print("The average of the lists is ")
print(avg_ages(ages_list))
print("The lowest age is ")
print(min_age(ages_list))
print("The highest age is ")
print(max_age(ages_list))
print("The list sorted and reversed is ")
print(reverse_sort(ages_list))
