def csv_parser(string):
    ret = ''
    inside = False
    escape = False
    for i, c in enumerate(string):
        if escape:
            escape = False
            continue
        if not inside:
            if c == ',':
                ret += '|'
            elif c == '"':
                inside = True
            # elif c == ' ':
            #     if ret == '' or ret[-1] == '|':
            #         continue
            #     now = i
            #     while now < len(string) and string[now] == ' ':
            #         now += 1
            #     if now == len(string) or string[now] == ',':
            #         continue
            #     ret += c
            else:
                ret += c
        else:
            if c == '"':
                if i + 1 != len(string) and string[i+1] == '"':
                    escape = True
                    ret += '"'
                else:
                    inside = False
            else:
                ret += c
    return ret


csv = '''John,Doe,120 jefferson st.,Riverside, NJ, 08075
Jack,McGinnis,220 hobo Av.,Phila, PA,09119
"John ""Da Man""",Repici,120 Jefferson St.,Riverside, NJ,08075
Stephen,Tyler,"7452 Terrace ""At the Plaza"" road",SomeTown,SD, 91234
,Blankman,,SomeTown, SD, 00298
"Joan ""the bone"", Anne",Jet,"9th, at Terrace plc",Desert City,CO,00123'''

lines = csv.split('\n')
for line in lines:
    print(csv_parser(line))
