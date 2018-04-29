

##Constants
global_prime = 10**9 + 7

player_const = 5
card_const = 3
pot_const = 2
bet_const = 7
dealer_const = 11
table_const = 13


##Mappings and Arrays

suit_Translation = {
                    0 : 'Spades',
                    1 : 'Hearts',
                    2 : 'Clubs',
                    3 : 'Diamonds'
                   }

name_Translation = {
                    0 : 'Ace',
                    1 : 'Two',
                    2 : 'Three',
                    3 : 'Four',
                    4 : 'Five',
                    5 : 'Six',
                    6 : 'Seven',
                    7 : 'Eight',
                    8 : 'Nine',
                    9 : 'Ten',
                    10: 'Jack',
                    11: 'Queen',
                    12: 'King'
                  }

id_Prefix = {
                2 : 'po',
                3 : 'ca',
                5 : 'pl',
                7 : 'bt',
                11: 'dl',
                13: 'ta'
            }

"""
preflop_Odds index guide (number ranges shown in interval notation)

index1 : number of players [0 - 10]
index2 : value of card1 [0 - 14]
index3 : value of card2 [0 - 14]
index4 : off hand numerical boolean [0 - 1]
"""
preflop_Odds = 	[
                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.5039],[0.3231,0.3011],[0.3356,0.3252],[0.3667,0.3195],[0.3875,0.3414],[0.3832,0.3522],[0.4044,0.3604],[0.4304,0.4089],[0.4396,0.4187],[0.487,0.4414],[0.5095,0.4803],[0.5368,0.5102],[0.5803,0.554]],
                        [[0,0],[0,0],[0.3315,0.3016],[0.0,0.5481],[0.3737,0.316],[0.3812,0.3364],[0.3912,0.3506],[0.3961,0.3643],[0.435,0.3802],[0.4276,0.3988],[0.471,0.4218],[0.4992,0.4534],[0.5147,0.4938],[0.5375,0.5109],[0.5922,0.5557]],
                        [[0,0],[0,0],[0.3486,0.3218],[0.367,0.3262],[0.0,0.5775],[0.3847,0.3509],[0.4205,0.366],[0.4064,0.3739],[0.4303,0.3821],[0.4259,0.4056],[0.4777,0.4317],[0.5058,0.4544],[0.5215,0.4939],[0.5536,0.5119],[0.5769,0.5643]],
                        [[0,0],[0,0],[0.3531,0.3148],[0.3627,0.3376],[0.3752,0.3475],[0.0,0.6115],[0.4173,0.371],[0.4364,0.3934],[0.4337,0.4036],[0.4591,0.4283],[0.4673,0.4341],[0.4867,0.4692],[0.5343,0.4955],[0.5391,0.5447],[0.5938,0.5681]],
                        [[0,0],[0,0],[0.372,0.3372],[0.3695,0.3469],[0.3911,0.3612],[0.415,0.3797],[0.0,0.6314],[0.4536,0.4195],[0.4487,0.4262],[0.4709,0.4409],[0.4961,0.4581],[0.4953,0.473],[0.5339,0.5114],[0.581,0.5412],[0.6168,0.5893]],
                        [[0,0],[0,0],[0.3796,0.3457],[0.4038,0.3643],[0.4097,0.3808],[0.4257,0.4019],[0.4422,0.411],[0.0,0.6735],[0.4779,0.4465],[0.497,0.4573],[0.5109,0.4752],[0.5227,0.4896],[0.5586,0.5237],[0.5698,0.5614],[0.6177,0.5811]],
                        [[0,0],[0,0],[0.4014,0.3751],[0.4069,0.3781],[0.4259,0.388],[0.4289,0.4101],[0.4579,0.4341],[0.4832,0.4563],[0.0,0.7081],[0.5173,0.4925],[0.5258,0.4994],[0.5402,0.5172],[0.5575,0.5384],[0.5871,0.57],[0.6136,0.5947]],
                        [[0,0],[0,0],[0.4167,0.3979],[0.4274,0.4062],[0.4297,0.4116],[0.4576,0.4221],[0.474,0.4463],[0.4905,0.4649],[0.5213,0.4882],[0.0,0.7312],[0.5239,0.5263],[0.5614,0.5328],[0.5921,0.5588],[0.6104,0.5856],[0.634,0.6244]],
                        [[0,0],[0,0],[0.4428,0.4238],[0.4417,0.4255],[0.4595,0.4358],[0.4716,0.4483],[0.5026,0.4566],[0.5032,0.4884],[0.5318,0.4896],[0.5474,0.5178],[0.0,0.7636],[0.577,0.5687],[0.5891,0.5812],[0.6143,0.6036],[0.638,0.6398]],
                        [[0,0],[0,0],[0.4623,0.4509],[0.4835,0.4509],[0.4886,0.4603],[0.5108,0.4659],[0.514,0.4671],[0.5409,0.4989],[0.5554,0.5171],[0.5461,0.5415],[0.5779,0.5619],[0.0,0.7833],[0.5957,0.5939],[0.6405,0.6235],[0.6645,0.6522]],
                        [[0,0],[0,0],[0.4857,0.4833],[0.52,0.4753],[0.5271,0.4912],[0.5232,0.5083],[0.549,0.5174],[0.5486,0.5278],[0.5752,0.5323],[0.605,0.5646],[0.5961,0.5796],[0.5952,0.5854],[0.0,0.8103],[0.6408,0.6326],[0.691,0.6586]],
                        [[0,0],[0,0],[0.5502,0.5141],[0.5468,0.5176],[0.548,0.5244],[0.5426,0.538],[0.5697,0.5482],[0.5754,0.5491],[0.5958,0.5695],[0.5926,0.5832],[0.6159,0.6113],[0.6518,0.6179],[0.6378,0.6277],[0.0,0.8335],[0.6704,0.6561]],
                        [[0,0],[0,0],[0.5717,0.5512],[0.5623,0.559],[0.5759,0.5656],[0.599,0.5671],[0.5853,0.5908],[0.601,0.5961],[0.6227,0.6127],[0.64,0.6189],[0.6543,0.6326],[0.6708,0.6443],[0.6803,0.6634],[0.6774,0.658],[0.0,0.8636]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.3157],[0.2198,0.1783],[0.2386,0.185],[0.2352,0.1987],[0.2503,0.2051],[0.2587,0.2085],[0.252,0.2245],[0.2641,0.2409],[0.2915,0.2501],[0.3034,0.2609],[0.3197,0.2896],[0.3508,0.318],[0.3761,0.349]],
                        [[0,0],[0,0],[0.2157,0.1825],[0.0,0.3361],[0.246,0.2031],[0.2358,0.2046],[0.2489,0.2199],[0.253,0.2264],[0.2619,0.2261],[0.2812,0.241],[0.2923,0.2595],[0.3125,0.279],[0.3384,0.3054],[0.3646,0.3178],[0.3877,0.3545]],
                        [[0,0],[0,0],[0.2249,0.1878],[0.2457,0.204],[0.0,0.3731],[0.2489,0.2197],[0.2731,0.2267],[0.27,0.2413],[0.2802,0.2409],[0.2912,0.2477],[0.3057,0.2687],[0.318,0.2854],[0.3427,0.314],[0.3698,0.3263],[0.3986,0.3666]],
                        [[0,0],[0,0],[0.2248,0.2025],[0.2481,0.2056],[0.2741,0.2199],[0.0,0.4079],[0.2714,0.2522],[0.2937,0.2569],[0.2896,0.2589],[0.3077,0.2689],[0.3098,0.2729],[0.3158,0.2934],[0.3571,0.3177],[0.38,0.3401],[0.4003,0.3673]],
                        [[0,0],[0,0],[0.2551,0.2026],[0.2588,0.2196],[0.2655,0.2342],[0.2811,0.2539],[0.0,0.4487],[0.3114,0.2746],[0.3035,0.2813],[0.3401,0.2786],[0.3361,0.2912],[0.3288,0.2937],[0.3591,0.3246],[0.3852,0.3462],[0.4148,0.3788]],
                        [[0,0],[0,0],[0.2575,0.2072],[0.2693,0.2224],[0.2758,0.2342],[0.2942,0.257],[0.3134,0.2693],[0.0,0.4695],[0.336,0.3041],[0.339,0.3037],[0.3477,0.3093],[0.3542,0.3153],[0.3651,0.3336],[0.3924,0.36],[0.4344,0.4001]],
                        [[0,0],[0,0],[0.276,0.2197],[0.2706,0.2267],[0.2818,0.2448],[0.2864,0.261],[0.3135,0.2787],[0.3278,0.2985],[0.0,0.5119],[0.3706,0.3276],[0.3738,0.3345],[0.3844,0.3381],[0.382,0.3472],[0.3984,0.3724],[0.4456,0.4003]],
                        [[0,0],[0,0],[0.2744,0.2312],[0.2735,0.2343],[0.2757,0.2484],[0.2972,0.2635],[0.3146,0.2786],[0.3477,0.3037],[0.3731,0.3379],[0.0,0.5594],[0.3816,0.3571],[0.4,0.3709],[0.3998,0.3825],[0.4248,0.3977],[0.459,0.4266]],
                        [[0,0],[0,0],[0.2855,0.2482],[0.3012,0.2535],[0.294,0.2671],[0.3079,0.2687],[0.3252,0.2824],[0.3424,0.3181],[0.3675,0.336],[0.3927,0.3546],[0.0,0.5973],[0.4358,0.3946],[0.4354,0.4133],[0.4611,0.4216],[0.4587,0.4446]],
                        [[0,0],[0,0],[0.3045,0.271],[0.3076,0.2705],[0.3233,0.2825],[0.3426,0.2931],[0.3377,0.2923],[0.3653,0.321],[0.3849,0.3502],[0.404,0.3665],[0.4208,0.4],[0.0,0.6308],[0.4534,0.4197],[0.474,0.4375],[0.4951,0.4695]],
                        [[0,0],[0,0],[0.3303,0.2904],[0.3406,0.294],[0.3444,0.3105],[0.3585,0.3131],[0.3539,0.3292],[0.3664,0.3301],[0.3987,0.3536],[0.4024,0.3822],[0.4483,0.4093],[0.4496,0.4236],[0.0,0.663],[0.4801,0.4431],[0.5078,0.4794]],
                        [[0,0],[0,0],[0.3557,0.3115],[0.354,0.3196],[0.3754,0.3356],[0.3785,0.3401],[0.3742,0.3485],[0.3929,0.3665],[0.403,0.3785],[0.4257,0.4006],[0.4544,0.4247],[0.4709,0.4421],[0.4757,0.451],[0.0,0.7038],[0.5187,0.4852]],
                        [[0,0],[0,0],[0.3925,0.3603],[0.3891,0.3615],[0.3953,0.3578],[0.4053,0.3807],[0.4136,0.3834],[0.4159,0.3972],[0.4458,0.4118],[0.4576,0.424],[0.4788,0.4529],[0.4853,0.4715],[0.4977,0.481],[0.5253,0.4841],[0.0,0.7506]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.2289],[0.1629,0.1206],[0.17,0.1276],[0.1776,0.1398],[0.1883,0.1436],[0.1917,0.1458],[0.1987,0.1555],[0.2081,0.1593],[0.2161,0.1754],[0.2306,0.1909],[0.2374,0.2004],[0.2532,0.2221],[0.2919,0.2527]],
                        [[0,0],[0,0],[0.1671,0.1229],[0.0,0.2482],[0.1835,0.1421],[0.183,0.1465],[0.2011,0.1481],[0.2068,0.1536],[0.2112,0.1585],[0.2048,0.1725],[0.2227,0.1804],[0.2338,0.1962],[0.2512,0.2124],[0.2655,0.2313],[0.2996,0.2533]],
                        [[0,0],[0,0],[0.1728,0.1334],[0.187,0.1388],[0.0,0.2676],[0.2029,0.1629],[0.2171,0.1674],[0.2166,0.1689],[0.2167,0.1747],[0.2193,0.1728],[0.2324,0.1867],[0.2353,0.1893],[0.2605,0.2195],[0.2673,0.2334],[0.3112,0.2653]],
                        [[0,0],[0,0],[0.1681,0.1389],[0.1894,0.1486],[0.2007,0.1596],[0.0,0.3037],[0.2182,0.1841],[0.2227,0.1861],[0.2189,0.1828],[0.2371,0.1881],[0.2257,0.1949],[0.2522,0.2081],[0.2682,0.2227],[0.2787,0.2384],[0.2939,0.2736]],
                        [[0,0],[0,0],[0.1851,0.1443],[0.199,0.1605],[0.2144,0.169],[0.2288,0.1842],[0.0,0.3279],[0.2456,0.2052],[0.2502,0.2072],[0.2479,0.2072],[0.2543,0.2106],[0.2532,0.2147],[0.2743,0.2325],[0.2985,0.2514],[0.3219,0.2792]],
                        [[0,0],[0,0],[0.1916,0.1472],[0.2052,0.1595],[0.2103,0.1738],[0.2194,0.1851],[0.2492,0.2078],[0.0,0.3602],[0.2674,0.2346],[0.2614,0.23],[0.2649,0.2381],[0.2675,0.2352],[0.2651,0.2397],[0.2911,0.2633],[0.3304,0.2888]],
                        [[0,0],[0,0],[0.1922,0.1551],[0.2071,0.1518],[0.2089,0.1713],[0.2273,0.1892],[0.2394,0.208],[0.2599,0.2335],[0.0,0.3866],[0.2905,0.2503],[0.292,0.252],[0.3047,0.2577],[0.2968,0.2676],[0.3146,0.2756],[0.3395,0.3145]],
                        [[0,0],[0,0],[0.195,0.1603],[0.2125,0.1708],[0.2105,0.17],[0.2254,0.1882],[0.2492,0.2095],[0.2569,0.2268],[0.284,0.2482],[0.0,0.4336],[0.3097,0.2775],[0.3079,0.2782],[0.3202,0.2866],[0.3374,0.2999],[0.3454,0.3156]],
                        [[0,0],[0,0],[0.2048,0.1703],[0.2262,0.1778],[0.2253,0.1881],[0.2355,0.1957],[0.259,0.2091],[0.2671,0.2309],[0.2991,0.2514],[0.3087,0.2776],[0.0,0.4661],[0.3534,0.3113],[0.3482,0.315],[0.361,0.3296],[0.385,0.3512]],
                        [[0,0],[0,0],[0.2253,0.1892],[0.2365,0.1929],[0.2413,0.1988],[0.2378,0.2062],[0.2493,0.2149],[0.2613,0.241],[0.2971,0.2612],[0.3213,0.2862],[0.3481,0.3106],[0.0,0.5184],[0.3635,0.3328],[0.3648,0.3489],[0.3905,0.3658]],
                        [[0,0],[0,0],[0.2365,0.2029],[0.2512,0.2085],[0.2455,0.2158],[0.2526,0.2238],[0.2759,0.2284],[0.2762,0.2412],[0.3044,0.2688],[0.3226,0.2894],[0.3554,0.3189],[0.3736,0.3308],[0.0,0.5505],[0.3959,0.3621],[0.4056,0.3777]],
                        [[0,0],[0,0],[0.2654,0.2228],[0.2623,0.2258],[0.2796,0.236],[0.2848,0.24],[0.291,0.2564],[0.3007,0.2609],[0.3106,0.2819],[0.3257,0.3043],[0.3592,0.3363],[0.3749,0.3411],[0.397,0.3617],[0.0,0.5996],[0.4324,0.4007]],
                        [[0,0],[0,0],[0.2975,0.2521],[0.3038,0.2646],[0.2949,0.2596],[0.3083,0.2688],[0.3068,0.2853],[0.3178,0.2958],[0.3437,0.3051],[0.3537,0.3276],[0.393,0.3539],[0.4025,0.3658],[0.4062,0.3771],[0.4276,0.3957],[0.0,0.6607]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.1875],[0.1372,0.0904],[0.1399,0.0976],[0.1467,0.1033],[0.1507,0.1079],[0.1483,0.1136],[0.1545,0.1157],[0.173,0.1213],[0.1817,0.1352],[0.189,0.1445],[0.1934,0.1565],[0.2139,0.1769],[0.2353,0.1993]],
                        [[0,0],[0,0],[0.1324,0.094],[0.0,0.1967],[0.1483,0.1058],[0.1554,0.1127],[0.1676,0.1142],[0.1677,0.1167],[0.1578,0.1168],[0.1712,0.1286],[0.1859,0.1343],[0.1934,0.1463],[0.1927,0.1602],[0.2209,0.1763],[0.2479,0.2043]],
                        [[0,0],[0,0],[0.1426,0.1022],[0.1502,0.106],[0.0,0.2135],[0.1618,0.1203],[0.1726,0.1311],[0.1761,0.1296],[0.1728,0.1315],[0.1671,0.1279],[0.1865,0.1393],[0.1959,0.1494],[0.2094,0.1667],[0.2288,0.1851],[0.2516,0.2063]],
                        [[0,0],[0,0],[0.1463,0.1045],[0.1609,0.1107],[0.1616,0.1214],[0.0,0.2313],[0.1808,0.1425],[0.1841,0.1434],[0.1777,0.1436],[0.1889,0.1421],[0.1968,0.1499],[0.2018,0.1633],[0.223,0.1692],[0.2424,0.1866],[0.2592,0.212]],
                        [[0,0],[0,0],[0.1455,0.1076],[0.1557,0.1197],[0.1641,0.1281],[0.1932,0.1446],[0.0,0.2559],[0.1996,0.1619],[0.2007,0.1602],[0.2075,0.162],[0.2005,0.1591],[0.2007,0.1594],[0.2233,0.1782],[0.2436,0.2012],[0.2569,0.2179]],
                        [[0,0],[0,0],[0.1491,0.1094],[0.1585,0.1223],[0.17,0.1388],[0.1815,0.1435],[0.1963,0.1623],[0.0,0.282],[0.2168,0.1749],[0.2232,0.18],[0.2299,0.1796],[0.2242,0.1857],[0.2224,0.1877],[0.2401,0.2055],[0.2664,0.224]],
                        [[0,0],[0,0],[0.1594,0.1178],[0.1566,0.1206],[0.1699,0.1309],[0.1868,0.1438],[0.1974,0.1599],[0.2166,0.1803],[0.0,0.3094],[0.2369,0.2023],[0.2487,0.2075],[0.2401,0.2071],[0.255,0.2101],[0.261,0.2175],[0.279,0.2408]],
                        [[0,0],[0,0],[0.1613,0.1227],[0.1712,0.1263],[0.1725,0.1322],[0.188,0.1436],[0.1943,0.1598],[0.2169,0.1881],[0.234,0.2013],[0.0,0.3339],[0.2591,0.2291],[0.2662,0.2326],[0.2646,0.2301],[0.2771,0.2432],[0.2923,0.2523]],
                        [[0,0],[0,0],[0.18,0.1287],[0.1828,0.1389],[0.1843,0.1449],[0.1911,0.146],[0.1997,0.1621],[0.2186,0.189],[0.2438,0.2076],[0.2654,0.231],[0.0,0.3798],[0.2967,0.2555],[0.2903,0.2673],[0.3094,0.272],[0.3212,0.2885]],
                        [[0,0],[0,0],[0.1849,0.1431],[0.1922,0.1427],[0.1976,0.1517],[0.1999,0.1568],[0.2003,0.1615],[0.2176,0.1811],[0.2459,0.2074],[0.2623,0.2275],[0.3002,0.2674],[0.0,0.4229],[0.3049,0.2831],[0.3277,0.2875],[0.3285,0.2988]],
                        [[0,0],[0,0],[0.2034,0.1543],[0.1972,0.1608],[0.2096,0.1664],[0.2116,0.1756],[0.2224,0.1774],[0.2327,0.1879],[0.2437,0.2126],[0.2749,0.2316],[0.2901,0.259],[0.3081,0.2811],[0.0,0.4615],[0.3456,0.3025],[0.3468,0.3149]],
                        [[0,0],[0,0],[0.2174,0.1748],[0.2168,0.1825],[0.2273,0.1833],[0.2284,0.1913],[0.2355,0.1948],[0.2518,0.2045],[0.2564,0.212],[0.2814,0.2382],[0.3039,0.2723],[0.3229,0.2857],[0.3273,0.3003],[0.0,0.5148],[0.37,0.3366]],
                        [[0,0],[0,0],[0.2336,0.1986],[0.2456,0.1997],[0.2459,0.2039],[0.2508,0.2121],[0.2682,0.219],[0.2648,0.2294],[0.2819,0.2391],[0.2927,0.2587],[0.3222,0.2859],[0.3367,0.3034],[0.3484,0.3116],[0.3654,0.3391],[0.0,0.5805]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.1613],[0.1218,0.074],[0.1252,0.0817],[0.1256,0.0813],[0.1268,0.0871],[0.1209,0.0904],[0.1347,0.0902],[0.1354,0.097],[0.156,0.1073],[0.16,0.116],[0.1652,0.1265],[0.1814,0.1449],[0.2017,0.1594]],
                        [[0,0],[0,0],[0.1197,0.0744],[0.0,0.1698],[0.1241,0.0859],[0.1367,0.0914],[0.1371,0.0987],[0.1364,0.0927],[0.1369,0.0967],[0.1423,0.1031],[0.1577,0.1121],[0.1628,0.1201],[0.1755,0.1323],[0.1778,0.1453],[0.2038,0.1621]],
                        [[0,0],[0,0],[0.1199,0.0791],[0.1263,0.0844],[0.0,0.181],[0.1403,0.1029],[0.1459,0.1069],[0.1508,0.1075],[0.1384,0.1056],[0.1466,0.1054],[0.1524,0.1124],[0.1669,0.1228],[0.1759,0.1321],[0.194,0.1521],[0.203,0.1684]],
                        [[0,0],[0,0],[0.1271,0.0826],[0.1342,0.0921],[0.1464,0.0975],[0.0,0.198],[0.1553,0.1161],[0.162,0.1185],[0.1605,0.1177],[0.1552,0.1187],[0.1593,0.1176],[0.1694,0.1262],[0.1827,0.1385],[0.198,0.1505],[0.2141,0.1736]],
                        [[0,0],[0,0],[0.13,0.09],[0.136,0.0984],[0.144,0.1076],[0.1524,0.1158],[0.0,0.2123],[0.1677,0.134],[0.1757,0.1329],[0.1718,0.1324],[0.1696,0.1317],[0.1748,0.1359],[0.1821,0.15],[0.2042,0.163],[0.2288,0.1772]],
                        [[0,0],[0,0],[0.126,0.0891],[0.1282,0.0958],[0.1419,0.1073],[0.1545,0.1184],[0.1748,0.131],[0.0,0.2346],[0.182,0.1471],[0.1869,0.1481],[0.1874,0.1513],[0.1916,0.1542],[0.1951,0.1529],[0.2147,0.1685],[0.2298,0.1862]],
                        [[0,0],[0,0],[0.1346,0.0928],[0.1371,0.0964],[0.1499,0.1044],[0.1599,0.1169],[0.1791,0.1321],[0.1878,0.1457],[0.0,0.2476],[0.2062,0.1641],[0.2126,0.1694],[0.2035,0.1709],[0.2139,0.1693],[0.2217,0.1725],[0.2446,0.2013]],
                        [[0,0],[0,0],[0.1487,0.0979],[0.141,0.1011],[0.1456,0.1044],[0.158,0.1179],[0.1678,0.1335],[0.1855,0.1521],[0.2078,0.1641],[0.0,0.2813],[0.2264,0.1931],[0.2229,0.1914],[0.2281,0.1913],[0.232,0.2008],[0.2413,0.2126]],
                        [[0,0],[0,0],[0.153,0.1068],[0.1491,0.1094],[0.1568,0.1155],[0.1554,0.1173],[0.1665,0.1324],[0.1875,0.1501],[0.2063,0.1732],[0.2225,0.1899],[0.0,0.3135],[0.2526,0.2253],[0.2538,0.2253],[0.2676,0.2285],[0.2741,0.243]],
                        [[0,0],[0,0],[0.1569,0.1174],[0.1577,0.116],[0.1722,0.1208],[0.1674,0.129],[0.1695,0.1291],[0.188,0.1505],[0.2183,0.1652],[0.228,0.1906],[0.2503,0.2203],[0.0,0.3543],[0.2648,0.2375],[0.2712,0.2443],[0.2945,0.2533]],
                        [[0,0],[0,0],[0.1627,0.1261],[0.1709,0.1281],[0.1785,0.1332],[0.1847,0.1361],[0.1878,0.1391],[0.192,0.1509],[0.2021,0.1723],[0.2252,0.1963],[0.2546,0.2238],[0.2682,0.2324],[0.0,0.3942],[0.2852,0.2601],[0.3007,0.2703]],
                        [[0,0],[0,0],[0.1865,0.1379],[0.1857,0.1418],[0.1848,0.1493],[0.194,0.1514],[0.2004,0.1632],[0.205,0.1682],[0.2234,0.1804],[0.2458,0.1995],[0.2601,0.23],[0.2792,0.24],[0.2975,0.2584],[0.0,0.4534],[0.3233,0.2943]],
                        [[0,0],[0,0],[0.1975,0.1593],[0.214,0.163],[0.2143,0.1704],[0.2184,0.1674],[0.2243,0.1741],[0.2338,0.1901],[0.2392,0.1995],[0.2465,0.2155],[0.2811,0.2434],[0.2886,0.2555],[0.3033,0.2704],[0.3281,0.2953],[0.0,0.5159]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.1502],[0.1038,0.0645],[0.109,0.0653],[0.1135,0.0698],[0.1152,0.075],[0.1175,0.0756],[0.1197,0.076],[0.1236,0.0851],[0.1286,0.0908],[0.1328,0.0963],[0.1486,0.1059],[0.1565,0.1204],[0.1839,0.1365]],
                        [[0,0],[0,0],[0.1019,0.0613],[0.0,0.1547],[0.117,0.073],[0.1135,0.0765],[0.1253,0.0829],[0.1228,0.0783],[0.1208,0.0821],[0.1249,0.0853],[0.1322,0.0888],[0.1435,0.0989],[0.1535,0.1085],[0.16,0.1215],[0.1805,0.1367]],
                        [[0,0],[0,0],[0.1082,0.0682],[0.1151,0.074],[0.0,0.1673],[0.1261,0.0874],[0.1311,0.0913],[0.1327,0.0887],[0.1268,0.086],[0.1233,0.088],[0.1348,0.094],[0.1433,0.0993],[0.1513,0.1109],[0.1675,0.1232],[0.1859,0.1416]],
                        [[0,0],[0,0],[0.1117,0.0684],[0.1092,0.0773],[0.124,0.0889],[0.0,0.1744],[0.1437,0.0993],[0.1395,0.0996],[0.1369,0.0974],[0.1357,0.0967],[0.1379,0.0977],[0.149,0.1039],[0.1576,0.1169],[0.172,0.1276],[0.1888,0.1434]],
                        [[0,0],[0,0],[0.1127,0.0745],[0.1184,0.0802],[0.1318,0.0915],[0.1373,0.0995],[0.0,0.1836],[0.1472,0.1121],[0.1505,0.1101],[0.1454,0.1108],[0.1522,0.1085],[0.1428,0.11],[0.1632,0.1155],[0.1772,0.1309],[0.1969,0.1514]],
                        [[0,0],[0,0],[0.111,0.0743],[0.1171,0.0801],[0.1272,0.0902],[0.1363,0.0995],[0.1527,0.1153],[0.0,0.2004],[0.1587,0.1253],[0.1677,0.1274],[0.1669,0.1253],[0.1603,0.1287],[0.1677,0.1253],[0.1778,0.1404],[0.1933,0.1554]],
                        [[0,0],[0,0],[0.1156,0.0784],[0.1202,0.0771],[0.1324,0.0895],[0.1376,0.0969],[0.1523,0.1119],[0.1619,0.1269],[0.0,0.211],[0.1751,0.1418],[0.1812,0.1482],[0.1789,0.14],[0.1911,0.1426],[0.1888,0.1467],[0.2114,0.1672]],
                        [[0,0],[0,0],[0.1249,0.0844],[0.1323,0.086],[0.1264,0.0862],[0.1375,0.0954],[0.1518,0.1108],[0.1593,0.1283],[0.1777,0.1381],[0.0,0.2362],[0.2009,0.1638],[0.2001,0.1638],[0.2032,0.1625],[0.2136,0.1688],[0.2172,0.1795]],
                        [[0,0],[0,0],[0.1313,0.091],[0.1357,0.0915],[0.1399,0.0949],[0.1461,0.0972],[0.15,0.1091],[0.1611,0.1255],[0.1805,0.1453],[0.2008,0.1686],[0.0,0.2621],[0.2226,0.1879],[0.2317,0.1923],[0.2326,0.1984],[0.2449,0.2081]],
                        [[0,0],[0,0],[0.1415,0.0989],[0.1493,0.0975],[0.1389,0.1],[0.1452,0.1032],[0.1586,0.1108],[0.1627,0.1225],[0.1772,0.141],[0.1995,0.1631],[0.2249,0.1909],[0.0,0.3031],[0.2383,0.2057],[0.2458,0.2076],[0.2595,0.2194]],
                        [[0,0],[0,0],[0.1503,0.1068],[0.147,0.108],[0.156,0.1118],[0.1594,0.1131],[0.1596,0.1205],[0.1662,0.1275],[0.1779,0.1414],[0.1983,0.1611],[0.2224,0.1898],[0.2315,0.2041],[0.0,0.3469],[0.2515,0.2283],[0.2743,0.2354]],
                        [[0,0],[0,0],[0.1657,0.1206],[0.1671,0.1228],[0.1621,0.1265],[0.1683,0.1273],[0.1785,0.1322],[0.1809,0.1422],[0.1905,0.1467],[0.2103,0.1682],[0.237,0.1974],[0.2457,0.2062],[0.2608,0.2276],[0.0,0.3939],[0.2971,0.2566]],
                        [[0,0],[0,0],[0.1822,0.1383],[0.1805,0.1405],[0.1949,0.1427],[0.1841,0.1445],[0.1876,0.1519],[0.195,0.1612],[0.2011,0.1744],[0.2229,0.1844],[0.2484,0.2064],[0.253,0.2231],[0.2767,0.2373],[0.2884,0.261],[0.0,0.4594]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.1401],[0.0973,0.0565],[0.0987,0.0574],[0.1042,0.0615],[0.1056,0.0641],[0.1009,0.0621],[0.1055,0.0643],[0.1082,0.0701],[0.1158,0.0774],[0.1255,0.0833],[0.1349,0.0925],[0.1523,0.1023],[0.16,0.1178]],
                        [[0,0],[0,0],[0.0974,0.0532],[0.0,0.1454],[0.1043,0.0622],[0.106,0.0676],[0.1113,0.0706],[0.1111,0.0671],[0.1071,0.066],[0.1181,0.0698],[0.1187,0.0777],[0.1233,0.0838],[0.1385,0.0954],[0.1466,0.1027],[0.1723,0.1196]],
                        [[0,0],[0,0],[0.0996,0.0565],[0.1029,0.0646],[0.0,0.1501],[0.1096,0.0755],[0.1166,0.0792],[0.1082,0.0793],[0.1165,0.0719],[0.1128,0.0735],[0.1233,0.0799],[0.1274,0.0861],[0.1384,0.0933],[0.1492,0.1055],[0.1676,0.1235]],
                        [[0,0],[0,0],[0.0983,0.0596],[0.1056,0.0665],[0.1161,0.0745],[0.0,0.1543],[0.1254,0.0865],[0.1267,0.0879],[0.1268,0.0857],[0.1207,0.0824],[0.1227,0.0832],[0.1325,0.0878],[0.1405,0.0979],[0.1573,0.1111],[0.1718,0.1244]],
                        [[0,0],[0,0],[0.0986,0.064],[0.1124,0.0706],[0.1175,0.0796],[0.1238,0.0863],[0.0,0.1627],[0.1386,0.1004],[0.1328,0.0973],[0.1327,0.094],[0.1354,0.0929],[0.1369,0.0908],[0.1414,0.1013],[0.154,0.1128],[0.171,0.1284]],
                        [[0,0],[0,0],[0.1053,0.0637],[0.109,0.0684],[0.1161,0.0789],[0.1279,0.0875],[0.1323,0.0995],[0.0,0.1755],[0.1526,0.1094],[0.1481,0.108],[0.1496,0.11],[0.1428,0.1052],[0.1446,0.1075],[0.1621,0.1183],[0.1796,0.1329]],
                        [[0,0],[0,0],[0.1119,0.0686],[0.1072,0.0706],[0.113,0.0741],[0.123,0.0856],[0.1327,0.0986],[0.1431,0.1085],[0.0,0.1846],[0.1602,0.1247],[0.1586,0.1276],[0.1631,0.1201],[0.1565,0.1252],[0.1697,0.1279],[0.1841,0.1466]],
                        [[0,0],[0,0],[0.1133,0.071],[0.1165,0.0708],[0.1105,0.0736],[0.1198,0.0855],[0.1367,0.0938],[0.1462,0.1068],[0.1548,0.1234],[0.0,0.2043],[0.1715,0.1463],[0.1715,0.1423],[0.1807,0.1419],[0.1808,0.1445],[0.1957,0.1557]],
                        [[0,0],[0,0],[0.1143,0.0756],[0.1197,0.0798],[0.1185,0.0813],[0.1215,0.0814],[0.1343,0.0949],[0.1483,0.1101],[0.1595,0.123],[0.1804,0.1465],[0.0,0.2299],[0.2035,0.1665],[0.1983,0.168],[0.2088,0.1695],[0.2132,0.1834]],
                        [[0,0],[0,0],[0.1279,0.0811],[0.1311,0.086],[0.131,0.087],[0.127,0.0873],[0.1356,0.0905],[0.1497,0.109],[0.1582,0.1216],[0.1743,0.1456],[0.196,0.1692],[0.0,0.2578],[0.2138,0.1768],[0.2189,0.1847],[0.2363,0.1935]],
                        [[0,0],[0,0],[0.1337,0.0916],[0.1309,0.093],[0.1398,0.095],[0.1369,0.0961],[0.1416,0.0998],[0.1509,0.1065],[0.1644,0.1219],[0.1864,0.1424],[0.1986,0.1658],[0.2138,0.1815],[0.0,0.3034],[0.2338,0.1993],[0.2502,0.2087]],
                        [[0,0],[0,0],[0.1489,0.1021],[0.1443,0.1065],[0.1456,0.105],[0.1469,0.1106],[0.1594,0.1164],[0.165,0.1201],[0.1687,0.1315],[0.1868,0.1449],[0.2113,0.1695],[0.2212,0.1878],[0.2375,0.199],[0.0,0.3467],[0.2626,0.2277]],
                        [[0,0],[0,0],[0.1651,0.1181],[0.163,0.1184],[0.1651,0.1237],[0.1711,0.1254],[0.1735,0.1285],[0.1766,0.1361],[0.1838,0.1436],[0.1899,0.1534],[0.2192,0.1794],[0.237,0.198],[0.2455,0.2075],[0.2592,0.2333],[0.0,0.4083]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.1349],[0.0888,0.0495],[0.0881,0.0517],[0.0923,0.0554],[0.0952,0.0565],[0.0975,0.0551],[0.0943,0.0579],[0.0995,0.0632],[0.1037,0.0674],[0.1099,0.0752],[0.1181,0.0804],[0.1317,0.0886],[0.1519,0.1025]],
                        [[0,0],[0,0],[0.0882,0.048],[0.0,0.1384],[0.0929,0.0566],[0.0976,0.0593],[0.1002,0.0626],[0.098,0.0607],[0.0986,0.0582],[0.0985,0.0628],[0.1114,0.0675],[0.1168,0.0748],[0.1242,0.0833],[0.1296,0.089],[0.1546,0.1051]],
                        [[0,0],[0,0],[0.0926,0.0513],[0.091,0.056],[0.0,0.1411],[0.1066,0.0654],[0.1076,0.0697],[0.1088,0.0663],[0.1031,0.0648],[0.1048,0.0647],[0.1096,0.0683],[0.1146,0.0739],[0.1264,0.0822],[0.1342,0.0921],[0.1548,0.1075]],
                        [[0,0],[0,0],[0.0896,0.0543],[0.0969,0.0597],[0.1082,0.0649],[0.0,0.1464],[0.1134,0.0765],[0.1099,0.077],[0.12,0.0749],[0.1087,0.0712],[0.1126,0.07],[0.1235,0.0762],[0.1275,0.0841],[0.1388,0.0933],[0.1537,0.1109]],
                        [[0,0],[0,0],[0.0936,0.0554],[0.0963,0.0615],[0.1075,0.0705],[0.1143,0.079],[0.0,0.151],[0.1274,0.0857],[0.1245,0.0853],[0.1174,0.0832],[0.1164,0.0795],[0.117,0.0798],[0.1275,0.0858],[0.1449,0.0954],[0.1523,0.1138]],
                        [[0,0],[0,0],[0.096,0.0551],[0.1023,0.0607],[0.1016,0.0688],[0.1192,0.0776],[0.1251,0.0856],[0.0,0.1599],[0.1298,0.0939],[0.1328,0.0943],[0.1326,0.095],[0.1307,0.0905],[0.1371,0.0917],[0.1469,0.1018],[0.1629,0.1222]],
                        [[0,0],[0,0],[0.0965,0.0585],[0.0949,0.0616],[0.1092,0.0668],[0.1122,0.0753],[0.1262,0.0883],[0.1313,0.0967],[0.0,0.1701],[0.1453,0.1096],[0.1406,0.1108],[0.1425,0.1072],[0.1496,0.1073],[0.1474,0.1104],[0.1732,0.128]],
                        [[0,0],[0,0],[0.0999,0.0608],[0.1033,0.0601],[0.1011,0.0629],[0.1114,0.0715],[0.1216,0.0812],[0.1322,0.0971],[0.141,0.1085],[0.0,0.1826],[0.1696,0.1267],[0.1643,0.1222],[0.1643,0.1228],[0.1691,0.1312],[0.1744,0.1361]],
                        [[0,0],[0,0],[0.1077,0.0678],[0.1069,0.069],[0.1119,0.0693],[0.1101,0.0699],[0.1217,0.0793],[0.1347,0.0935],[0.1433,0.1098],[0.1615,0.1242],[0.0,0.2017],[0.1823,0.1478],[0.1806,0.1473],[0.1847,0.1513],[0.1953,0.161]],
                        [[0,0],[0,0],[0.1092,0.0744],[0.1137,0.0718],[0.1159,0.0752],[0.1185,0.0786],[0.1188,0.0782],[0.132,0.0914],[0.1523,0.1052],[0.1643,0.1234],[0.1789,0.1484],[0.0,0.2282],[0.1982,0.1589],[0.2042,0.1646],[0.2081,0.1707]],
                        [[0,0],[0,0],[0.12,0.0785],[0.1273,0.0805],[0.1283,0.0833],[0.1232,0.0833],[0.1294,0.0869],[0.1297,0.0951],[0.1439,0.1052],[0.1595,0.1254],[0.1835,0.1489],[0.1917,0.1585],[0.0,0.2621],[0.2135,0.1776],[0.2257,0.1904]],
                        [[0,0],[0,0],[0.1332,0.0896],[0.1367,0.0906],[0.1347,0.0945],[0.137,0.0962],[0.1428,0.0977],[0.1502,0.1021],[0.1526,0.1128],[0.167,0.1295],[0.1843,0.1511],[0.1984,0.165],[0.2122,0.179],[0.0,0.3089],[0.2367,0.2076]],
                        [[0,0],[0,0],[0.1476,0.1062],[0.1521,0.1052],[0.1533,0.1057],[0.1574,0.1091],[0.1562,0.1124],[0.1688,0.1189],[0.173,0.1254],[0.1825,0.135],[0.1962,0.1594],[0.2109,0.1734],[0.2189,0.1891],[0.243,0.2065],[0.0,0.3708]]
                    ],

                    [
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                        [[0,0],[0,0],[0.0,0.1294],[0.0811,0.0458],[0.0828,0.0481],[0.0829,0.0477],[0.0903,0.0523],[0.0862,0.0479],[0.0925,0.0485],[0.0934,0.054],[0.0993,0.0584],[0.1038,0.0635],[0.1135,0.0711],[0.1194,0.0781],[0.1391,0.0915]],
                        [[0,0],[0,0],[0.0827,0.0448],[0.0,0.132],[0.0865,0.05],[0.0923,0.0539],[0.0926,0.0545],[0.094,0.0532],[0.0894,0.0514],[0.0952,0.0552],[0.0946,0.06],[0.1054,0.0658],[0.1159,0.0714],[0.1234,0.0805],[0.1405,0.0919]],
                        [[0,0],[0,0],[0.0821,0.0465],[0.0871,0.0499],[0.0,0.1365],[0.0967,0.0595],[0.1011,0.0629],[0.1,0.0603],[0.0967,0.0586],[0.0936,0.0549],[0.0966,0.0629],[0.1066,0.0666],[0.1138,0.0729],[0.1215,0.0828],[0.1397,0.094]],
                        [[0,0],[0,0],[0.0851,0.0503],[0.0944,0.0534],[0.0944,0.0593],[0.0,0.1409],[0.1054,0.0732],[0.1079,0.0712],[0.1024,0.0668],[0.1047,0.0619],[0.1028,0.0626],[0.1073,0.0671],[0.1109,0.0756],[0.1256,0.0847],[0.1404,0.0976]],
                        [[0,0],[0,0],[0.0823,0.0511],[0.0922,0.0548],[0.1023,0.0622],[0.1102,0.0703],[0.0,0.1416],[0.113,0.0788],[0.1081,0.0772],[0.1101,0.0739],[0.1142,0.0698],[0.1164,0.0704],[0.1189,0.0775],[0.1268,0.086],[0.1401,0.101]],
                        [[0,0],[0,0],[0.0865,0.0509],[0.0908,0.054],[0.1008,0.0612],[0.1058,0.0692],[0.1138,0.0776],[0.0,0.1473],[0.1241,0.0878],[0.1234,0.0859],[0.1188,0.084],[0.1189,0.0808],[0.1236,0.0783],[0.1306,0.0896],[0.1414,0.1068]],
                        [[0,0],[0,0],[0.0854,0.0517],[0.0938,0.0519],[0.0946,0.058],[0.107,0.0665],[0.1148,0.0771],[0.1222,0.0874],[0.0,0.1517],[0.1338,0.0965],[0.1362,0.0971],[0.1328,0.0991],[0.1319,0.0935],[0.1398,0.0973],[0.1519,0.1114]],
                        [[0,0],[0,0],[0.087,0.053],[0.0932,0.0546],[0.0954,0.0556],[0.103,0.0625],[0.1124,0.0741],[0.1228,0.0857],[0.1319,0.0975],[0.0,0.1685],[0.1516,0.114],[0.1477,0.1117],[0.1485,0.1079],[0.1463,0.1143],[0.16,0.1151]],
                        [[0,0],[0,0],[0.0978,0.0594],[0.099,0.0604],[0.1008,0.0614],[0.1046,0.063],[0.1126,0.07],[0.1271,0.0854],[0.1313,0.0975],[0.149,0.1141],[0.0,0.1834],[0.1723,0.1366],[0.1714,0.1312],[0.1713,0.1335],[0.1885,0.1446]],
                        [[0,0],[0,0],[0.1043,0.0644],[0.1075,0.0626],[0.1028,0.0651],[0.1106,0.0671],[0.1121,0.0697],[0.1193,0.0827],[0.1315,0.097],[0.1436,0.1085],[0.17,0.1332],[0.0,0.205],[0.1781,0.1414],[0.1901,0.1444],[0.1914,0.1539]],
                        [[0,0],[0,0],[0.1122,0.0724],[0.118,0.0694],[0.1131,0.0731],[0.1111,0.0749],[0.1179,0.0761],[0.1192,0.0825],[0.1308,0.0917],[0.1471,0.1108],[0.1739,0.134],[0.1733,0.1401],[0.0,0.2402],[0.1976,0.1582],[0.1987,0.1674]],
                        [[0,0],[0,0],[0.1267,0.0796],[0.1234,0.0805],[0.1281,0.0795],[0.1243,0.0832],[0.1315,0.0874],[0.1325,0.0905],[0.1354,0.0949],[0.1537,0.1098],[0.1769,0.1356],[0.1855,0.1445],[0.196,0.1579],[0.0,0.2777],[0.2225,0.1868]],
                        [[0,0],[0,0],[0.1363,0.0919],[0.1398,0.0938],[0.1347,0.0951],[0.1371,0.0958],[0.1472,0.0993],[0.1446,0.1042],[0.1544,0.1119],[0.1606,0.12],[0.1807,0.1438],[0.1852,0.1546],[0.2018,0.1675],[0.2188,0.1848],[0.0,0.3367]]]
                ]
