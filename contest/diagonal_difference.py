def diagonalDifference(arr):
    main_diag, second_diag = 0, 0
    for i in range(len(arr)):
        main_diag += arr[i][i]
        second_diag += arr[(len(arr)-i-1)][i]
    return abs(main_diag - second_diag)