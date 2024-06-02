from foo_parameterization import foo

class TestFoo():
    def test_run(self):
        assert foo(1) == 4.1887902047863905
        assert foo(0) == 0.0
        try:
            foo(-1)
            assert False, "Expected ValueError"
        except ValueError:
            pass
    
if __name__ == "__main__":
    test = TestFoo()
    test.test_run()