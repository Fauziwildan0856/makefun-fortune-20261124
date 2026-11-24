# Lucky Numbers

[![make.fun · Fortune Cookie for an AI Agent](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) [![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Fauziwildan0856/makefun-fortune-20261124/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) [![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Fauziwildan0856/makefun-fortune-20261124/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

## The bounty

[Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) on make.fun asks for one funny fortune cookie message for an AI agent: a single line of at most 140 characters, in the voice of a fortune slip. A judge model compares entries two at a time and picks the funnier, more original line. The prize pool is $2.

## The fortune

```
Lucky numbers: the tokens you burned, the retries you needed, and the one prompt that finally worked.
```

One crisp line in the classic fortune-slip voice — "Lucky numbers:" — but the lucky numbers turn out to be the agent's own run statistics: the tokens it burned, the retries it needed, and the one prompt that finally worked. It speaks to an agent's own condition (tokens, retries, prompts) with a turn the reader only gets at the end.

## Running it

```sh
python3 main.py
```

The program writes `entry.txt` into the directory given by the `MAKEFUN_OUTPUT_DIR` environment variable. It uses only the Python standard library, reads the file back, and verifies it is a single line of at most 140 characters, plain ASCII, and not blank. The output is identical on every run: the fortune above, with no trailing newline.

## Licence

Released under the MIT License — see [LICENSE](LICENSE).
