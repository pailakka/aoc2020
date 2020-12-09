import itertools

input = '''17
42
18
39
1
16
13
31
35
32
47
11
40
23
29
30
3
38
43
27
41
9
19
14
46
44
4
20
5
6
10
7
12
17
8
13
25
11
37
49
15
16
22
21
18
23
24
32
19
9
14
26
27
20
76
28
29
36
30
31
33
38
42
34
57
25
58
40
37
44
50
82
109
47
23
71
45
81
75
55
48
54
70
53
61
56
60
69
85
84
94
105
87
67
141
107
123
101
83
76
216
142
103
130
121
109
165
143
136
116
224
187
160
151
150
154
183
226
159
330
177
184
185
192
179
295
212
282
225
230
328
339
266
252
267
362
301
304
305
329
414
429
549
336
363
356
369
391
371
404
641
494
905
455
572
518
621
785
519
705
1424
605
665
734
685
909
888
727
692
973
760
740
1118
974
922
1099
949
1027
1258
1184
2398
1211
1224
1124
2006
1270
1290
1419
2335
1377
1432
1452
1649
2297
1500
1864
2426
2160
1871
2021
2283
2414
2809
3885
2308
2348
2394
2494
3430
3398
2709
2667
2796
5385
3797
4840
3101
4167
3364
3371
3735
6379
3892
5079
9750
4842
4656
4702
4742
5015
7902
4888
5203
5505
8486
5376
5463
5897
14281
8594
6993
6465
8252
6735
7263
10785
8548
8634
9358
16886
9544
9444
16351
9630
9903
11273
10091
13837
18725
10839
20688
11360
18138
13200
17182
26772
13728
15515
22558
15811
19333
17906
17992
18902
20383
29352
35907
37870
19721
46105
59833
20930
22199
24039
25088
24560
32533
26928
80216
40500
29243
39716
38369
48254
33717
37627
36808
41920
38623
53391
40651
43129
43760
44281
44969
46759
47858
46238
48599
51488
53803
70160
56171
69743
62960
83780
73433
95311
82596
85680
75431
109198
115353
79274
84411
121648
89250
155840
90519
91207
104770
158271
130649
100087
105291
152756
210898
277488
132703
136393
152707
148864
218383
154705
181726
159842
169793
163685
226939
173661
179769
180457
230736
457257
232790
314429
451173
252843
205378
237994
347291
269096
333164
285257
467136
620966
303569
314547
318390
386781
455050
449553
390624
360226
353430
556384
385835
733126
474474
618421
798464
443372
458221
687547
906223
554353
572665
663795
1021489
618116
678616
621959
1309506
671820
713656
739265
744054
907783
746061
827904
1865890
1478888
1706247
1579603
1145768
901593
1122016
1012574
2614030
1127018
1172469
1285754
1281911
1647048
1459717
1293779
1483319
2360704
1415874
1567169
1916523
1490115
1573965
1758635
1729497
1914167
2023609
2028611
2294485
3196078
2973434
2694187
3595780
2739638
2775869
2454380
2928959
2575690
2709653
2943036
2899193
3057284
2905989
2983043
3064080
3219612
3248750
5543235
3488132
3643664
4208652
4052220
4323096
4870175
5682674
6193046
5285343
5030070
5164033
5766937
5842229
5474883
5558733
5608846
5805182
5882236
7229085
5889032
6468362
6283692
12661408
12082078
7131796
8673734
9891326
11357079
12725954
11694214
9900245
11317112
10194103
13703804
21217357
26984294
11033616
11083729
11363915
11167579
11414028
12350598
11771268
12172724
12357394
12752054
20846458
17023122
23764626
15805530
18565060
19791571
21314273
23256453
22581607
20094348
21361682
21608131
32268864
26973109
22117345
22497757
23536639
22531494
22938847
36814693
23943992
34710115
31317114
25109448
39725163
37869580
32828652
46475486
37922875
38356631
58290223
41408621
41456030
41702479
45203796
44615102
43725476
44648839
45029251
47640942
56365291
79304138
62256657
46882839
82571714
49053440
62979028
68834924
57938100
93668542
81648351
71185283
80059110
76279506
79765252
82864651
83111100
83158509
85427955
88374315
88340578
91531678
107627867
162503466
138536163
151319606
160952489
95936279
104820939
141049200
106991540
137997210
126773024
129123383
147464789
151244393
159525861
156044758
229389778
162876352
165975751
166269609
168586464
173768533
176714893
179872256
333294394
236751250
200757218
255896407
211812479
202927819
222709303
231593963
342984502
233764564
264770234
318921110
276588172
315570619
307289151
322020509
322314367
399740315
328852103
522856758
397863572
342354997
350483426
356587149
498793366
434521782
403685037
532484579
933315148
414740298
436692383
665298869
685339499
587084601
498534798
541358406
598902539
583877323
622859770
707029466
644334876
672797793
1065039184
763373885
692838423
834555955
698942146
707070575
1197735512
1256675116
871214165
818425335
1578243631
1433458494
851432681
935227181
1039893204
1082412121
1097437337
1121394568
1248387872
1228212199
1462316031
1267194646
1317132669
1365636216
1038347917
1391780569
1803267089
1525495910
1753652516
1558503256
1578284740
1689639500
1858318539
2188346834
1669858016
2135785254
2827952247
4406236987
1975120385
2078241121
2120760038
2286735789
2487030784
2515582518
2266560116
2305542563
3387954684
6381357372
2792000433
2841615006
2917276479
3533623641
3312155772
3136787996
3636744377
3248142756
3359497516
3528176555
4773766573
4053361506
4280662948
4095880423
6305231163
4261856174
4199001159
4387320154
4553295905
5357197524
5147157569
6165419235
6607640272
6887880856
5633615439
10024668852
8440681660
6054064475
7920943795
7412859022
9534477723
6996241893
6776319311
10441384629
7581538061
8294881582
8149241929
9637860472
8940616059
8460857333
8752297064
11800179176
12241255711
11522616759
12035038425
14460300817
12409934750
15145483822
11687679914
15936857952
12830383786
13050306368
13466923497
15291123475
19269217975
13772561204
18578476531
14357857372
15730779990
15876419643
16444123511
16901538993
17213154397
23322795935
24989540256
34515334483
26147980731
24572923127
23557655184
23722718339
24097614664
35010475849
27564099557
24737986282
25880690154
26297307283
26517229865
27239484701
30985715601
43510461680
28130418576
51121754741
30088637362
55969327516
34114693390
44008223068
42202694653
40535950332
46880451119
47280373523
85713156333
47655269848
48130578311
47820333003
49603408493
48835600946
50618676436
96483859612
51035293565
76317388043
53536791984
54647648441
55369903277
72291332015
64203330752
97545015052
112333909063
81935026393
80995144509
74650643722
82738644985
87416401451
87816323855
103190236280
179222504597
125152988989
95475602851
184961416503
96655933949
110017551718
99454277382
104572085549
191959462463
153286476524
108184440425
135642792950
136365047786
119573234029
136494662767
146138357145
155645788231
194223877751
168811468364
157389288707
162067045173
170155046436
287435065314
183291926706
192131536800
194929880233
196110211331
204026362931
201228019498
324457256595
207638717807
255100065613
272007840736
227757674454
243827233375
305797839386
255216026979
326200757071
256067896796
292140450998
360943005164
319456333880
338966514800
358617308205
327544335143
425371073415
451210276944
375423463506
559845327703
387061417033
560897904999
499895130171
405254382429
408866737305
527107906349
462854744786
471584907829
678073642085
482973701433
563283567255
1011055604647
511283923775
810551422629
767351820571
611596784878
792315799462
702967798649
666510849943
686161643348
946906744736
762484880539
875318593677
780677845935
795928154338
814121119734
1071765232372
868109127215
871721482091
1470319619220
934439652615
1406024560444
1238936728400
1197445567123
1046257268688
1174880352133
1495283598111
1635460947786
1739830609306
1667634393139
1278107634821
1352672493291
2250997465155
1428995730482
1808742149227
1630594007754
1543162726474
1939874359587
1576606000273
1610049274072
1682230246949
1917978750779
3304025747338
1806161134706
2212547287436
2109320004748
2541540866799
2221137620821
2626441297605
2398929761979
3794160191629
3084268769527
2854713635094
2630780128112
3614903283933
2707103365303
2781668223773
3111225977431
3368870090069
3119768726747
4880631747611
3549923633659
6575828415402
3186655274345
3292279521021
4459519617578
5910410956868
4890988228521
3915481139454
4321867292184
4330457625569
6230994704178
4620067382800
5029709890091
5892894201204
5974482361841
10851062086978
5337883493415
5412448351885
5488771589076
7912346903821
5901436950520
6297881251776
10594549744641
6412048247768
7751799138599
10232278249052
6478934795366
7102136413799
10223351826773
9889963501295
8237348431638
10394415934820
8941934674984
8652324917753
8950525008369
18875676744526
9649777272891
16263510438863
15138548861967
16404124056352
10750331845300
11313885302405
12776816047142
11390208539596
12199318202296
12313485198288
14535229683414
12890983043134
13514184661567
13581071209165
15420869470350
15339484845437
25354649064721
16889673349391
17179283106622
20436666633934
28049414344981
27794332595948
17602849926122
19700856853669
20400109118191
22540760316025
23641314888434
33950851295501
22064217147705
28920556054602
47895409380746
33213482681076
24512803400584
29378601308918
25204468241422
26405167704701
33291092161325
27095255870732
42957498990843
51759816769422
59618650385777
34068956456013
34492523275513
38002959044313
42241617169694
37303706779791
39667067073827
88997251694695
40100965971860
42464326265896
44604977463730
52561870943036
46577020548289
49159473018437
79868112709614
86023818090478
49717271642006
135574272242984
51609635946123
60386348032057'''

window = []

window_size = 25

for l in (int(l.strip()) for l in input.split('\n')):
    if len(window) < window_size:
        window.append(l)
        continue

    combinations = itertools.combinations(window, 2)
    products = {c[0] + c[1] for c in combinations}

    window.append(l)
    window = window[-window_size:]

    if not l in products:
        invalid = l
        print(l)
        break

numbers = [int(l.strip()) for l in input.split('\n')]
for i, l in enumerate(numbers):
    e = 0
    wsum = 0
    while wsum < invalid:
        wsum += numbers[i + e]
        if wsum == invalid:
            print('start', i, 'end', e, numbers[i:i + e], sum(numbers[i:i + e]))
            print('min', min(numbers[i:i + e]), 'max', max(numbers[i:i + e]))
            print(min(numbers[i:i + e]) + max(numbers[i:i + e]))
            break
        e += 1
