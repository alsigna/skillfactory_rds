(
    lambda __g, __print: [
        [
            [
                [
                    (
                        lambda __after: [
                            (
                                r.raise_for_status(),
                                (
                                    lambda __after: (
                                        __print(
                                            ("secret code3:", hashlib.md5(requests.__name__.encode()).hexdigest()[:5])
                                        ),
                                        __after(),
                                    )[1]
                                    if ((r.status_code == 200) and (int((r.json()["prediction"] * 10000)) == ___()))
                                    else (__print("wrong answer"), __after())[1]
                                )(lambda: __after()),
                            )[1]
                            for __g["r"] in [
                                (requests.post("http://127.0.0.1:5000/predict", json=[1, 1, 1, 21.121217366373163]))
                            ]
                        ][0]
                        if (__name__ == "__main__")
                        else __after()
                    )(lambda: None)
                    for __g["___"], ___.__name__ in [(lambda: (seven() * 10101), "___")]
                ][0]
                for __g["seven"] in [((lambda: 13))]
            ][0]
            for __g["requests"] in [(__import__("requests", __g, __g))]
        ][0]
        for __g["hashlib"] in [(__import__("hashlib", __g, __g))]
    ][0]
)(globals(), __import__("builtins", level=0).__dict__["print"])
