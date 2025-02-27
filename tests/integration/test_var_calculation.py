import numpy as np
from numpy.ma.testutils import assert_equal

from src.var_calculation import calculate_1d_shift, calculate_pnl_vector_1d, calculate_historical_var_1d, \
    calculate_parametric_var_1d, calculate_total_var_1d


def test_fx_portfolio_var_calculation():
    # Given
    spot_portfolio_values = [153084.81, 95891.51]
    currency1_daily_market_rates: np.ndarray = np.array([1.1684427,
                                                         1.165976797,
                                                         1.16603118,
                                                         1.166901992,
                                                         1.160725686,
                                                         1.160712213,
                                                         1.162466288,
                                                         1.162020521,
                                                         1.158050769,
                                                         1.159084323,
                                                         1.160995205,
                                                         1.156992283,
                                                         1.160671797,
                                                         1.159164938,
                                                         1.157420803,
                                                         1.157126161,
                                                         1.158761979,
                                                         1.15928588,
                                                         1.164903779,
                                                         1.157889862,
                                                         1.155081202,
                                                         1.158426394,
                                                         1.157836236,
                                                         1.141630705,
                                                         1.148791471,
                                                         1.115299681,
                                                         1.112743134,
                                                         1.114876918,
                                                         1.12083749,
                                                         1.119870991,
                                                         1.129318231,
                                                         1.124062813,
                                                         1.119733056,
                                                         1.128935752,
                                                         1.124492573,
                                                         1.12731946,
                                                         1.129496809,
                                                         1.130867236,
                                                         1.133758437,
                                                         1.135151089,
                                                         1.129484052,
                                                         1.128579006,
                                                         1.129905201,
                                                         1.129292724,
                                                         1.124151266,
                                                         1.123458883,
                                                         1.122258883,
                                                         1.118918677,
                                                         1.116220922,
                                                         1.11477749,
                                                         1.116245842,
                                                         1.105534305,
                                                         1.103046615,
                                                         1.099601944,
                                                         1.103022281,
                                                         1.10282765,
                                                         1.103387399,
                                                         1.010123245,
                                                         1.099747058,
                                                         1.104899123,
                                                         1.105546527,
                                                         1.093469798,
                                                         1.094235567,
                                                         1.093637219,
                                                         1.093744873,
                                                         1.090655266,
                                                         1.082508822,
                                                         1.078865034,
                                                         1.077156737,
                                                         1.07820199,
                                                         1.083247576,
                                                         1.083505791,
                                                         1.087961704,
                                                         1.085422772,
                                                         1.091381361,
                                                         1.098490674,
                                                         1.096234287,
                                                         1.090905124,
                                                         1.098719991,
                                                         1.113337787,
                                                         1.119670369,
                                                         1.121642084,
                                                         1.11564808,
                                                         1.113647753,
                                                         1.114243373,
                                                         1.112978442,
                                                         1.107162232,
                                                         1.106304831,
                                                         1.111296327,
                                                         1.116196004,
                                                         1.114293037,
                                                         1.1105805,
                                                         1.112433671,
                                                         1.115672974,
                                                         1.114504157,
                                                         1.114789918,
                                                         1.113635351,
                                                         1.115038525,
                                                         1.117006423,
                                                         1.114050958,
                                                         1.115050958,
                                                         1.114541422,
                                                         1.117355889,
                                                         1.117218573,
                                                         1.121453404,
                                                         1.124985938,
                                                         1.126164172,
                                                         1.120925436,
                                                         1.118480656,
                                                         1.123204277,
                                                         1.125365744,
                                                         1.124163903,
                                                         1.124075448,
                                                         1.121239643,
                                                         1.125163149,
                                                         1.127116161,
                                                         1.130467222,
                                                         1.12847712,
                                                         1.127471982,
                                                         1.1281843,
                                                         1.131528922,
                                                         1.133542661,
                                                         1.134404211,
                                                         1.132964742,
                                                         1.132618274,
                                                         1.135976372,
                                                         1.134803282,
                                                         1.14310536,
                                                         1.140706097,
                                                         1.14087528,
                                                         1.144348065,
                                                         1.147802532,
                                                         1.152113552,
                                                         1.154921119,
                                                         1.158842548,
                                                         1.159393405,
                                                         1.160294715,
                                                         1.16638479,
                                                         1.169590643,
                                                         1.172525385,
                                                         1.165324601,
                                                         1.163995297,
                                                         1.16132379,
                                                         1.157407407,
                                                         1.57284634,
                                                         1.568324628,
                                                         1.156590833,
                                                         1.154227937,
                                                         1.152963693,
                                                         1.156122826,
                                                         1.156925355,
                                                         1.154521105,
                                                         1.155214639,
                                                         1.159729551,
                                                         1.158158065,
                                                         1.160739159,
                                                         1.163277651,
                                                         1.157420803,
                                                         1.158721698,
                                                         1.159218687,
                                                         1.166412,
                                                         1.171687347,
                                                         1.164225674,
                                                         1.170686022,
                                                         1.168346532,
                                                         1.164646006,
                                                         1.172374175,
                                                         1.171440286,
                                                         1.165555504,
                                                         1.171550078,
                                                         1.150483203,
                                                         1.161737029,
                                                         1.169057389,
                                                         1.165949608,
                                                         1.17249789,
                                                         1.174853437,
                                                         1.169590643,
                                                         1.161642563,
                                                         1.166520852,
                                                         1.158506916,
                                                         1.16780138,
                                                         1.162007019,
                                                         1.159810255,
                                                         1.163372384,
                                                         1.16295297,
                                                         1.16512094,
                                                         1.171508903,
                                                         1.165311022,
                                                         1.151768541,
                                                         1.151330939,
                                                         1.151410478,
                                                         1.151012891,
                                                         1.149729239,
                                                         1.143301397,
                                                         1.140693085,
                                                         1.133118796,
                                                         1.14153948,
                                                         1.140133852,
                                                         1.140914329,
                                                         1.142739604,
                                                         1.142400183,
                                                         1.139211666,
                                                         1.134198349,
                                                         1.144885225,
                                                         1.14187839,
                                                         1.143379831,
                                                         1.144112398,
                                                         1.148349572,
                                                         1.15036409,
                                                         1.155374804,
                                                         1.148567162,
                                                         1.14825064,
                                                         1.140797189,
                                                         1.134751773,
                                                         1.135383078,
                                                         1.134134032,
                                                         1.128515325,
                                                         1.119482351,
                                                         1.125707789,
                                                         1.117143687,
                                                         1.108696616,
                                                         1.107125459,
                                                         1.112644087,
                                                         1.1141813,
                                                         1.115026092,
                                                         1.106060103,
                                                         1.110592834,
                                                         1.117156167,
                                                         1.109299256,
                                                         1.107910481,
                                                         1.110975325,
                                                         1.114305453,
                                                         1.1105805,
                                                         1.106831363,
                                                         1.10702741,
                                                         1.111716379,
                                                         1.112334679,
                                                         1.111790539,
                                                         1.112099644,
                                                         1.113833816,
                                                         1.106427236,
                                                         1.101770545,
                                                         1.12027245,
                                                         1.123048133,
                                                         1.123078133,
                                                         1.1212145,
                                                         1.122498232,
                                                         1.122384843,
                                                         1.122120359,
                                                         1.130671732,
                                                         1.128387985,
                                                         1.130965845,
                                                         1.128795575,
                                                         1.128349788,
                                                         1.121730157,
                                                         1.123898579,
                                                         1.247645328,
                                                         1.126722477,
                                                         1.129598879,
                                                         1.14998045])
    currency2_daily_market_rates: np.ndarray = np.array([0.886564121,
                                                         0.884329678,
                                                         0.883470271,
                                                         0.87753938,
                                                         0.877658927,
                                                         0.876270592,
                                                         0.877654906,
                                                         0.876693114,
                                                         0.881600987,
                                                         0.881911985,
                                                         0.885700368,
                                                         0.886839305,
                                                         0.878271562,
                                                         0.879816998,
                                                         0.881290209,
                                                         0.880902044,
                                                         0.88163985,
                                                         0.878464444,
                                                         0.87788605,
                                                         0.879198171,
                                                         0.883197174,
                                                         0.879700902,
                                                         0.881329044,
                                                         0.885151582,
                                                         0.88210647,
                                                         0.879971841,
                                                         0.875465091,
                                                         0.876001927,
                                                         0.876270592,
                                                         0.876193814,
                                                         0.876616261,
                                                         0.876923751,
                                                         0.874431619,
                                                         0.873667657,
                                                         0.880824452,
                                                         0.877654906,
                                                         0.876424189,
                                                         0.872600349,
                                                         0.873896705,
                                                         0.868809731,
                                                         0.867829558,
                                                         0.871269876,
                                                         0.872105699,
                                                         0.874087671,
                                                         0.87753938,
                                                         0.878734622,
                                                         0.87966221,
                                                         0.879894413,
                                                         0.88051422,
                                                         0.878811846,
                                                         0.880630531,
                                                         0.877308418,
                                                         0.874469853,
                                                         0.87507623,
                                                         0.875273523,
                                                         0.87001914,
                                                         0.871991629,
                                                         0.874928912,
                                                         0.876501008,
                                                         0.878889084,
                                                         0.880630531,
                                                         0.882768362,
                                                         0.886839305,
                                                         0.884955752,
                                                         0.886014265,
                                                         0.886839305,
                                                         0.887941751,
                                                         0.884564352,
                                                         0.882339966,
                                                         0.881057269,
                                                         0.881290209,
                                                         0.881911985,
                                                         0.881367883,
                                                         0.88028169,
                                                         0.878618811,
                                                         0.876232202,
                                                         0.878194432,
                                                         0.883119177,
                                                         0.884603476,
                                                         0.883587365,
                                                         0.890194507,
                                                         0.890234132,
                                                         0.890947969,
                                                         0.88691796,
                                                         0.884173298,
                                                         0.884642604,
                                                         0.883002208,
                                                         0.882028666,
                                                         0.881406725,
                                                         0.880902044,
                                                         0.88028169,
                                                         0.886367665,
                                                         0.883197174,
                                                         0.886485528,
                                                         0.888967908,
                                                         0.88999644,
                                                         0.890323,
                                                         0.891067053,
                                                         0.893535272,
                                                         0.890511599,
                                                         0.891583452,
                                                         0.89098766,
                                                         0.887981175,
                                                         0.88711466,
                                                         0.888809884,
                                                         0.88711466,
                                                         0.883821645,
                                                         0.884407889,
                                                         0.884955752,
                                                         0.884760009,
                                                         0.889363216,
                                                         0.889086464,
                                                         0.888533475,
                                                         0.892299456,
                                                         0.892538379,
                                                         0.8942312,
                                                         0.89512332,
                                                         0.89561596,
                                                         0.8952134,
                                                         0.889600569,
                                                         0.894134478,
                                                         0.893894699,
                                                         0.893255918,
                                                         0.893854749,
                                                         0.892538379,
                                                         0.89047195,
                                                         0.889263216,
                                                         0.889363216,
                                                         0.891901534,
                                                         0.892259648,
                                                         0.89465444,
                                                         0.896137647,
                                                         0.89561596,
                                                         0.894374385,
                                                         0.896619744,
                                                         0.896901206,
                                                         0.892458724,
                                                         0.893575194,
                                                         0.894854586,
                                                         0.897504936,
                                                         0.898714838,
                                                         0.897021887,
                                                         0.892618049,
                                                         0.89031339,
                                                         0.887862914,
                                                         0.886406949,
                                                         0.882067566,
                                                         0.883704489,
                                                         0.883743538,
                                                         0.883431247,
                                                         0.887232721,
                                                         0.890868597,
                                                         0.890789239,
                                                         0.894054537,
                                                         0.891583452,
                                                         0.885778821,
                                                         0.883314195,
                                                         0.878040214,
                                                         0.878425861,
                                                         0.879043601,
                                                         0.879584836,
                                                         0.878889084,
                                                         0.883041194,
                                                         0.885269122,
                                                         0.885367665,
                                                         0.886367665,
                                                         0.891106755,
                                                         0.891543708,
                                                         0.892379083,
                                                         0.888888889,
                                                         0.888730892,
                                                         0.888691402,
                                                         0.887862914,
                                                         0.891106755,
                                                         0.890828916,
                                                         0.891662951,
                                                         0.891106755,
                                                         0.891027355,
                                                         0.896860987,
                                                         0.897424392,
                                                         0.896097495,
                                                         0.898795614,
                                                         0.898311175,
                                                         0.897786955,
                                                         0.90244334,
                                                         0.90440445,
                                                         0.900738606,
                                                         0.894054537,
                                                         0.893974611,
                                                         0.891662951,
                                                         0.89273758,
                                                         0.892777431,
                                                         0.89146423,
                                                         0.893694982,
                                                         0.896860987,
                                                         0.900252071,
                                                         0.900576369,
                                                         0.901225667,
                                                         0.901794571,
                                                         0.901388138,
                                                         0.902445628,
                                                         0.900009,
                                                         0.899806542,
                                                         0.901243,
                                                         0.902934537,
                                                         0.903628067,
                                                         0.906043309,
                                                         0.911701691,
                                                         0.912325518,
                                                         0.906618314,
                                                         0.905387053,
                                                         0.905223138,
                                                         0.904486252,
                                                         0.905715062,
                                                         0.909338911,
                                                         0.906700517,
                                                         0.902282775,
                                                         0.909256228,
                                                         0.904977376,
                                                         0.90424089,
                                                         0.904568069,
                                                         0.908265213,
                                                         0.90962735,
                                                         0.91124248,
                                                         0.912575287,
                                                         0.913993236,
                                                         0.913408842,
                                                         0.916674306,
                                                         0.916086479,
                                                         0.913575735,
                                                         0.910332271,
                                                         0.910829766,
                                                         0.909545682,
                                                         0.912825194,
                                                         0.910705341,
                                                         0.908182726,
                                                         0.905879156,
                                                         0.907029478,
                                                         0.906084356,
                                                         0.904813608,
                                                         0.899523253,
                                                         0.897585495,
                                                         0.897182846,
                                                         0.898391879,
                                                         0.899523253,
                                                         0.900414191,
                                                         0.901631954,
                                                         0.901550667,
                                                         0.899604174,
                                                         0.899118864,
                                                         0.896539358,
                                                         0.895255148,
                                                         0.896458987,
                                                         0.903097625,
                                                         0.903056847,
                                                         0.912825194,
                                                         0.910705341,
                                                         0.900414191,
                                                         0.905879156,
                                                         0.895255148
                                                         ])
    confidence_level = 0.99

    # When
    currency1_1d_shifts: np.ndarray = np.array([
        calculate_1d_shift(float(currency1_daily_market_rates[i - 1]), float(currency1_daily_market_rates[i]))
        for i in range(1, len(currency1_daily_market_rates))
    ])
    currency2_1d_shifts: np.ndarray = np.array([
        calculate_1d_shift(float(currency2_daily_market_rates[i - 1]), float(currency2_daily_market_rates[i]))
        for i in range(1, len(currency2_daily_market_rates))
    ])
    currency1_1d_pnl_vectors: np.ndarray = np.array([
        calculate_pnl_vector_1d(shift, spot_portfolio_values[0])
        for shift in currency1_1d_shifts
    ])
    currency2_1d_pnl_vectors: np.ndarray = np.array([
        calculate_pnl_vector_1d(shift, spot_portfolio_values[1])
        for shift in currency2_1d_shifts
    ])
    total_pnl_vectors: np.ndarray = currency1_1d_pnl_vectors + currency2_1d_pnl_vectors
    historical_var_value_1d: float = calculate_historical_var_1d(total_pnl_vectors, confidence_level)
    parametric_var_value_1d: float = calculate_parametric_var_1d(total_pnl_vectors, confidence_level)
    var_value_1d: float = calculate_total_var_1d(total_pnl_vectors)

    # Then
    assert_equal(historical_var_value_1d, -6753.44)
    assert_equal(parametric_var_value_1d, -10917.30)
    assert_equal(var_value_1d, -13572.73)
