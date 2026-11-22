"Core Basics complete program: Tuples & Sets"

def main():
    from collections import namedtuple

    Student = namedtuple("Student", "name group")
    records = (Student("Mira", "A"), Student("Roy", "B"))
    records += (Student("Ada", "A"),)
    records = records[:1] + (records[1]._replace(group="A"),) + records[2:]
    for name, group in records:
        print(name, group)
    first, *others = records
    print("Lead:", first.name, "others:", len(others))
    print("Record lookup:", records.index(first), records.count(first))
    registered = {r.name for r in records}
    present = {"Roy"}
    present.add("Mira")
    present.update(["Guest"])
    snapshot = present.copy()
    present.discard("Late")
    present.remove("Guest")
    print("Seen:", sorted(present | snapshot))
    print("Verified:", sorted(registered & present))
    print("Absent:", sorted(registered - present))
    print("Mismatch:", sorted(snapshot ^ registered))
    print("Complete:", registered.issubset(present), "Mira" in present)
    for name in sorted(present):
        print("Badge:", name)


if __name__ == "__main__":
    main()
