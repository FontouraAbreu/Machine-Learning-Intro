import numpy as np


def normal_eqn(X, y):
    # X transposto
    XT = X.T
    XTX = np.dot(XT, X)

    # Calcula a pseudoinversa de (XT * X)
    XTX_inv = np.linalg.pinv(XTX)

    # XT * y
    XTy = np.dot(XT, y)

    # Multiplica tudo para obter theta
    theta = np.dot(XTX_inv, XTy)

    return theta
