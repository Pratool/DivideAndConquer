def local_min(matrix):
    """
    Assume matrix as a list of lists containing integer or floating point
    values with NxN values.
    """

    if len(matrix) == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        sort = sorted([a, b, c, d])
        return sort[0] != sort[3]

    mid = int(len(matrix)/2.0)
    min_window_val = float("inf")
    min_window_index = (0,0)

    top_row = matrix[0]
    mid_row = matrix[mid]
    bottom_row = matrix[len(matrix)-1]
    for c in range(len(matrix[0])):
        if top_row[c] < min_window_val:
            min_window_val = top_row[c]
            min_window_index = (0, c)
        if mid_row[c] < min_window_val:
            min_window_val = mid_row[c]
            min_window_index = (mid, c)
        if bottom_row[c] < min_window_val:
            min_window_val = bottom_row[c]
            min_window_index = (len(matrix)-1, c)

    for r in range(1, mid-1):
        if matrix[r][0] < min_window_val:
            min_window_val = matrix[r][0]
            min_window_index = (r, 0)
        if matrix[r][mid] < min_window_val:
            min_window_val = matrix[r][mid]
            min_window_index = (r, mid)
        if matrix[r][len(matrix[r])-1] < min_window_val:
            min_window_val = matirx[r][len(matrix[r])-1]
            min_window_index = (r, len(matrix[r])-1)

    for r in matrix[mid+1:len(matrix)-1]:
        if matrix[r][0] < min_window_val:
            min_window_val = matrix[r][0]
            min_window_index = (r, 0)
        if matrix[r][mid] < min_window_val:
            min_window_val = matrix[r][mid]
            min_window_index = (r, mid)
        if matrix[r][len(matrix[r])-1] < min_window_val:
            min_window_val = matirx[r][len(matrix[r])-1]
            min_window_index = (r, len(matrix[r])-1)
    
    is_top = min_window_index[0] == 0
    is_bottom = min_window_index[0] == (len(matrix[0])-1)
    is_left = min_window_index[1] == 0
    is_right = min_window_index[1] == (len(matrix)-1)

    in_topleft = (min_window_index[0] <= mid) and (min_window_index[1] <= mid)
    in_topright = (min_window_index[0] <= mid) and (min_window_index[1] >= mid)
    in_bottomleft = (min_window_index[0] >= mid) and (min_window_index[1] <= mid)
    in_bottomright = (min_window_index[0] >= mid) and (min_window_index[1] >= mid)

    if not is_top and\
            matrix[min_window_index[0]-1][min_window_index[1]] < min_window_val:
        # Look at the value one row above minimum
        return recursive_call_matrix(in_topleft, in_topright, in_bottomleft,\
                mid, len(matrix[0]))
    elif not is_bottom and\
            matrix[min_window_index[0]+1][min_window_index[1]] < min_window_val:
        # Look at the value one row below minimum
        return recursive_call_matrix(in_topleft, in_topright, in_bottomleft,\
                mid, len(matrix[0]))
    elif not is_left and\
            matrix[min_window_index[0]][min_window_index[1]-1] < min_window_val:
        # Look at the value one column left of minimum
        return recursive_call_matrix(in_topleft, in_topright, in_bottomleft,\
                mid, len(matrix[0]))
    elif not is_right and\
            matrix[min_window_index[0]][min_window_index[1]+1] < min_window_val:
        # Look at the value one one column right of minimum
        return recursive_call_matrix(in_topleft, in_topright, in_bottomleft,\
                mid, len(matrix[0]))
    else:
        return True

def recursive_call_matrix(in_topleft, in_topright, in_bottomleft,\
        in_bottomright, mid, rownums):
    quadrants = [in_topleft, in_topright, in_bottomleft, in_bottomright]
    row_splices = [(0, mid+1), (0, mid+1), (mid, rownums), (mid, rownums)]
    col_splices = [(0, mid+1), (mid, rownums), (0, mid+1), (mid, rownums)]
    for (quadrant, row_splice, col_splice) in\
            zip(quadrants, row_splices, col_splices):
        rec_matrix = []
        if quadrant:
            for row in matrix[row_splice[0]:row_splice[1]]:
                rec_matrix.append(row[col_splice[0]:col_splice[1]])
            if local_min(rec_matrix):
                return True
    return False

a = [[5, 4, 3, 4], [2, 1, 0, 1], [1, 2, 3, 4], [5, 6, 7, 8]]
print local_min(a)
b = [[0]*4]*4
print local_min(b)
