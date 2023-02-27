"""
Project: Appointment

Author: Isabella Cortez

Credits: Lauren Mathews

Description: defines two classes and runs through test cases. there should be 0 errors for 5 tests
"""

from datetime import datetime

class Appt:

    def __init__(self, start: datetime, finish: datetime, desc: str):
        """An appointment from start time to finish time, with description desc.
        Start and finish should be the same day.
        """
        assert finish > start, f"Period finish ({finish}) must be after start ({start})"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __eq__(self, other: 'Appt') -> bool:
        """Equality means same time period, ignoring description"""
        return self.start == other.start and self.finish == other.finish

    def __lt__(self, other: 'Appt') -> bool:
        """returns whether finish is less than or equal to finish"""
        return self.finish <= other.start

    def __gt__(self, other: 'Appt') -> bool:
        """returns whether or not start is greater than or equal to finish"""
        return self.start >= other.finish

    def overlaps(self, other: 'Appt') -> bool:
        """Is there a non-zero overlap between these periods?"""
        if self.finish <= other.start or self.start >= other.finish:
            return False
        else:
            return True

    def intersect(self, other: 'Appt') -> 'Appt':
        """The overlapping portion of two Appt objects"""
        assert self.overlaps(other)  # Precondition
        newStart = max(self.start, other.start)
        newFinish = min(self.finish, other.finish)
        return Appt(newStart, newFinish, "na")

    def __str__(self) -> str:
        """The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm  | description
        Note that this is accurate only if start and finish
        are on the same day.
        """
        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"

    def __repr__(self) -> str:
        """this method controls formatting"""
        return f"Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})"


class Agenda:
    """An Agenda is a collection of appointments,
        similar to a list.

        Usage:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
        agenda = Agenda()
        agenda.append(appt1)
        agenda.append(appt2)
        ag_conflicts = agenda.conflicts()
        if len(ag_conflicts) == 0:
            print(f"Agenda has no conflicts")
        else:
            print(f"In agenda:\n{agenda.text()}")
            print(f"Conflicts:\n {ag_conflicts}")

        Expected output:
        In agenda:
        2018-03-15 13:30 15:30 | Early afternoon nap
        2018-03-15 15:00 16:00 | Coffee break
        Conflicts:
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
        """

    def __init__(self):
        """the elements in the appointment"""
        self.elements = []

    def __eq__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        return self.elements == other.elements

    def __len__(self):
        """distinguishes whether or not an agenda is free of conflict"""
        return len(self.elements)

    def append(self, appointment) -> list:
        """adds the elements to the appointment list"""
        self.elements.append(appointment)

    def __str__(self):
        """Each Appt on its own line"""
        lines = [str(e) for e in self.elements]
        return "\n".join(lines)

    def __repr__(self) -> str:
        """The constructor does not actually work this way"""
        return f"Agenda({self.elements})"

    def conflicts(self) -> 'Agenda':
        """Returns an agenda consisting of the conflicts
        (overlaps) between this agenda and the other.
        Side effect: This agenda is sorted
        """
        conflict = Agenda()
        self.sort()
        for item1 in range(len(self.elements)):
            for item2 in range(item1 + 1, len(self.elements)):
                if self.elements[item1].overlaps(self.elements[item2]):
                    conflict.append(self.elements[item1].intersect(self.elements[item2]))
                else:
                    break

        return conflict

    def start_time(appt: Appt) -> datetime:
        """returns the appointment times"""
        return appt.start

    def sort(self):
        """Sort agenda by appointment start times"""
        self.elements.sort(key=lambda appt: appt.start)

    def test_1_fast(self):
        """A linear time algorithm should be able to test
        an agenda with 5000 elements in well under a second,
        even on a fairly slow computer.
        """
        time_before = time.perf_counter()
        self.assertTrue(self.big.unconflicted())
        time_after = time.perf_counter()
        elapsed_seconds = time_after - time_before
        self.assertLess(elapsed_seconds, 2, "Are you sure your algorithm is linear time?")
        log.debug(f"Checked {len(self.big)} entries in {elapsed_seconds} seconds")

if __name__ == "__main__":
    """main driver program"""
    print("Running usage examples")
