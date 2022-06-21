import nox


@nox.session(python=["3.10", "3.9"])
def test(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
