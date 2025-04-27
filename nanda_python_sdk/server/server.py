from typing import Literal

from pydantic import BaseModel, EmailStr, HttpUrl


class Paramter(BaseModel):
    name: str
    description: str
    type: str
    required: bool
    default: str


class Capability(BaseModel):
    name: str
    description: str
    type: Literal["agent", "resource", "tool"]
    parameters: list[Paramter]
    examples: list[str]


class UsageRequirements(BaseModel):
    authentication_required: bool = False
    authentication_type: str = "none"
    rate_limits: str = ""
    pricing: str = ""


class Server(BaseModel):
    name: str
    slug: str
    description: str
    provider: str
    url: str
    documentation_url: str | None = None
    types: list[Literal["agent", "resource", "tool"]]
    tags: list[str] | None = None
    logo: str | None = None
    capabilities: list[Capability] | None = None
    protocols: list[str] | None = None
    usage_requirements: UsageRequirements = UsageRequirements()
    contact_email: EmailStr
