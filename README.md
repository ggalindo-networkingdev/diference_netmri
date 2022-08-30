# Introduction
## Purpose
[Describe the purpose for this project and its intended audience.]

## Scope
[Describe the scope which this automation will cover and what it will not cover.]

## Definitions, Acronyms, Abbreviations
- Airplane - An airplane or aeroplane (informally plane) is a fixed-wing aircraft that is propelled forward by thrust from a jet engine, propeller, or rocket engine.
- Truck - Any of various heavy motor vehicles designed for carrying or pulling loads.

## Assumptions
[Describe any assumptions which impact this project]

## References
[Detail any outside references for this document]

# Design
## Functional Description
[Describe the automation and high-level states.]

## Requirements
[Detail any requirements which need to be included in the automation]

## Input
[Describe the inputs used for the automation.]

## Output/Reporting
[Describe the expected outputs.]

[Describe any logging/reporting requirements for the automation]

## User Interface
[Describe how a user will interface with the system]

## Verifications
[Describe any required verifications to be included in the automation]

## Unit Tests
[Describe unit tests which should be included in the CI/CD pipeline]


# Software Details
## System interfaces
[Describe any outside services required for this project. Examples: Infoblox, ISE, NetMRI, SNOW, ect]

 
| Service | Service Address | Port | Protocol | Integration method   |
| ------------ | ------------ | ------------ | ------------ | ------------ |
|  |  |  |  | Ex: RESTful API |
|  |  |  |  | Ex: Webhook |
|  |  |  |  |  |

# Security
## Confidential Information handling
[If any credentials are required how will they be handled. Ex: Vault, service accounts, Environment variables ,user prompt]

## User Access
[Describe how users will access the systems in this project.]

## Security Rules
[Describe any firewall or other security exceptions required in this project]

| Source Host Name | Source IP | Source NAT IP | Destination Host Name | Destination IP Address | Data Classification Level | Dest NAT IP | TCP Ports | UDP Ports | Comments |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| example | 169.255.255.255 | | contoso.com | 169.255.255.254 | | | 443 | | Contoso.com website |
| | | | | | | | | |  |

## Encryption
[Description of what encryption will be used in the project. Example: Disk, file, transfer protocols, ect]