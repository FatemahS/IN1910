from exp_decay import ExponentialDecay

def test_call():
    tol = 1E-6
    a = 0.4; u = 3.2; du = -1.28

    InitialValues = ExponentialDecay(a)
    success = (abs(InitialValues(0,u) - (du)) < tol)

    assert success, "Call function does not give right solution."
