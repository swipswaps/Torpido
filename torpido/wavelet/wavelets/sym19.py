""" Symlet 19 wavelet """


class Symlet19:
    """
    Properties
    ----------
     near symmetric, orthogonal, biorthogonal

    All values are from http://wavelets.pybytes.com/wavelet/sym19/
    """
    __name__ = "Symlet Wavelet 19"
    __motherWaveletLength__ = 38  # length of the mother wavelet
    __transformWaveletLength__ = 2  # minimum wavelength of input signal

    # decomposition filter
    # low-pass
    decompositionLowFilter = [
        5.487732768215838e-07,
        -6.463651303345963e-07,
        -1.1880518269823984e-05,
        8.873312173729286e-06,
        0.0001155392333357879,
        -4.612039600210587e-05,
        -0.000635764515004334,
        0.00015915804768084938,
        0.0021214250281823303,
        -0.0011607032572062486,
        -0.005122205002583014,
        0.007968438320613306,
        0.01579743929567463,
        -0.02265199337824595,
        -0.046635983534938946,
        0.0070155738571741596,
        0.008954591173043624,
        -0.06752505804029409,
        0.10902582508127781,
        0.578144945338605,
        0.7195555257163943,
        0.2582661692372836,
        -0.17659686625203097,
        -0.11624173010739675,
        0.09363084341589714,
        0.08407267627924504,
        -0.016908234861345205,
        -0.02770989693131125,
        0.004319351874894969,
        0.008262236955528255,
        -0.0006179223277983108,
        -0.0017049602611649971,
        0.00012930767650701415,
        0.0002762187768573407,
        -1.6821387029373716e-05,
        -2.8151138661550245e-05,
        2.0623170632395688e-06,
        1.7509367995348687e-06,
    ]

    # high-pass
    decompositionHighFilter = [
        -1.7509367995348687e-06,
        2.0623170632395688e-06,
        2.8151138661550245e-05,
        -1.6821387029373716e-05,
        -0.0002762187768573407,
        0.00012930767650701415,
        0.0017049602611649971,
        -0.0006179223277983108,
        -0.008262236955528255,
        0.004319351874894969,
        0.02770989693131125,
        -0.016908234861345205,
        -0.08407267627924504,
        0.09363084341589714,
        0.11624173010739675,
        -0.17659686625203097,
        -0.2582661692372836,
        0.7195555257163943,
        -0.578144945338605,
        0.10902582508127781,
        0.06752505804029409,
        0.008954591173043624,
        -0.0070155738571741596,
        -0.046635983534938946,
        0.02265199337824595,
        0.01579743929567463,
        -0.007968438320613306,
        -0.005122205002583014,
        0.0011607032572062486,
        0.0021214250281823303,
        -0.00015915804768084938,
        -0.000635764515004334,
        4.612039600210587e-05,
        0.0001155392333357879,
        -8.873312173729286e-06,
        -1.1880518269823984e-05,
        6.463651303345963e-07,
        5.487732768215838e-07,
    ]

    # reconstruction filters
    # low pass
    reconstructionLowFilter = [
        1.7509367995348687e-06,
        2.0623170632395688e-06,
        -2.8151138661550245e-05,
        -1.6821387029373716e-05,
        0.0002762187768573407,
        0.00012930767650701415,
        -0.0017049602611649971,
        -0.0006179223277983108,
        0.008262236955528255,
        0.004319351874894969,
        -0.02770989693131125,
        -0.016908234861345205,
        0.08407267627924504,
        0.09363084341589714,
        -0.11624173010739675,
        -0.17659686625203097,
        0.2582661692372836,
        0.7195555257163943,
        0.578144945338605,
        0.10902582508127781,
        -0.06752505804029409,
        0.008954591173043624,
        0.0070155738571741596,
        -0.046635983534938946,
        -0.02265199337824595,
        0.01579743929567463,
        0.007968438320613306,
        -0.005122205002583014,
        -0.0011607032572062486,
        0.0021214250281823303,
        0.00015915804768084938,
        -0.000635764515004334,
        -4.612039600210587e-05,
        0.0001155392333357879,
        8.873312173729286e-06,
        -1.1880518269823984e-05,
        -6.463651303345963e-07,
        5.487732768215838e-07,
    ]

    # high-pass
    reconstructionHighFilter = [
        5.487732768215838e-07,
        6.463651303345963e-07,
        -1.1880518269823984e-05,
        -8.873312173729286e-06,
        0.0001155392333357879,
        4.612039600210587e-05,
        -0.000635764515004334,
        -0.00015915804768084938,
        0.0021214250281823303,
        0.0011607032572062486,
        -0.005122205002583014,
        -0.007968438320613306,
        0.01579743929567463,
        0.02265199337824595,
        -0.046635983534938946,
        -0.0070155738571741596,
        0.008954591173043624,
        0.06752505804029409,
        0.10902582508127781,
        -0.578144945338605,
        0.7195555257163943,
        -0.2582661692372836,
        -0.17659686625203097,
        0.11624173010739675,
        0.09363084341589714,
        -0.08407267627924504,
        -0.016908234861345205,
        0.02770989693131125,
        0.004319351874894969,
        -0.008262236955528255,
        -0.0006179223277983108,
        0.0017049602611649971,
        0.00012930767650701415,
        -0.0002762187768573407,
        -1.6821387029373716e-05,
        2.8151138661550245e-05,
        2.0623170632395688e-06,
        -1.7509367995348687e-06,
    ]