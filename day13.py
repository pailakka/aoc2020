from operator import itemgetter

input = '''1007268
17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,397,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'''

input = '''1068773
67,7,59,61'''

starttst, timetable = input.split('\n')
starttst = int(starttst)

timetable_offsets = [(i, int(bus), int(bus) + i) for i, bus in enumerate(timetable.split(',')) if bus != 'x']
timetable = [int(bus) for bus in timetable.split(',') if bus != 'x']

print('starttst', starttst)
print('timetable', timetable)

waittimes = ((bus, bus - starttst % bus, (bus - starttst % bus) * bus) for bus in timetable)
waittimes = sorted(waittimes, key=itemgetter(1))
print(waittimes, waittimes[0][2])

print('timetable_offsets', timetable_offsets)

f = timetable_offsets[0][1]
n = f
for o2, v2, _ in timetable_offsets[1:]:
    cv = v2 - o2
    while n % v2 != cv:
        n += f
    f *= v2
print(n)
