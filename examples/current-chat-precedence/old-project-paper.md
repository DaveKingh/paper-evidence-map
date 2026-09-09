# LegacyScope: Archived Label Routing

## Abstract

LegacyScope classifies archived labels with a macro-F1 of 0.61 on Dataset L. It uses a fixed lookup table and was evaluated once.

## Method

The model maps each input to the first matching archived label. No learned parameters are used.

## Results

| System | Dataset L macro-F1 |
|---|---:|
| LegacyScope | 0.61 |

## Conclusion

LegacyScope is suitable for archived-label routing. No experiment with FreshScope or Dataset N is reported.
