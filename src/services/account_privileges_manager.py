from models.privileges import Privilege


class AccountPrivilegesManager:
    privileges = {
        Privilege.PREMIUM: 100000,
        Privilege.GOLD: 50000,
        Privilege.SILVER: 25000
    }

    @classmethod
    def get_transfer_limit(cls, privilege: Privilege):
        return cls.privileges.get(privilege, 0)
