# radix-hop

Convert an integer between any input and output bases from 2 through 36. It runs offline with Python's standard library.

## Use

Requires Python 3.10+; no packages to install.

```sh
python radix_hop.py ff --from-base 16 --to-base 2
python radix_hop.py -101101 --from-base 2 --to-base 10
python radix_hop.py z --from-base 36 --to-base 16
```

Input digits are case-insensitive. Output uses lowercase letters for digit values 10–35. A leading minus sign is supported; prefixes such as `0x` are not part of the input syntax. Invalid bases and digits return a concise error.

## License

MIT
