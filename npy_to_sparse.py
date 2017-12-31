import numpy as np
mat = np.load('./ref_matrix.npy')
from scipy import sparse
sp = sparse.csr_matrix(mat)
sparse.save_npz('ref_matrix', sp)