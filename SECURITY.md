# Security Policy

## Reporting a vulnerability

Email **security@ab2bc.com** with:
- Description and impact
- Reproduction steps
- Suggested mitigation (if any)
- Your preferred disclosure timeline

We aim to acknowledge within 24 hours and publish a fix or mitigation
within 30 days for critical issues.

## Scope

In scope:
- AB2BC chains: AQY, ASY, AUY, AIY, ARY, AGO, ABC
- Smart contracts in `ab2bcSC/` (Move modules, bonds, bridge, marketplace, governance)
- Genesis RPC proxy and signing service
- red-envelope PWA wallet (`re.ab2bc.com`)
- Backend services: M2C-Backend, auy-utility, asy-securities, aiy-hitech, abc-issuance, qr-payment-api

Out of scope (already known / by design):
- Demo / staging environments not at `*.ab2bc.com`
- Self-XSS, missing security headers without exploit chain
- Social engineering of staff

## Bug bounty

A formal program is being established. In the interim, ad-hoc rewards are
available for verified critical findings — contact security@ab2bc.com.
