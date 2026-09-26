from federated_unilora.config import parse_args


def main() -> None:
    args = parse_args()
    from federated_unilora.train.federated import run_federated_experiment

    run_federated_experiment(args)


if __name__ == "__main__":
    main()
