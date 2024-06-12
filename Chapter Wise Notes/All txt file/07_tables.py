for i in range(2, 21):
    with open(f"tables\Multiplaction_table_of {i} .txt", 'w') as f:
        for m in range(1, 11):
            f.write(f"{i}X{m}={i*m}")
            if m != 10:
                    f.write('\n')
                    