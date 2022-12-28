from service.api.enums import ActionEnum
from service.factories import (
    FeatureActionFactory,
    FeatureFactory,
    RoleFactory,
    UserFactory,
    UserPermissionFactory, RolePermissionFactory,
)
from service.orm import FeatureModel


class MachinesGroup:
    group: FeatureModel
    machines_feature: FeatureModel
    devices_feature: FeatureModel
    machine_stock_feature: FeatureModel
    machine_planograms_feature: FeatureModel
    planogram_analysis_feature: FeatureModel
    machine_meter_readings_feature: FeatureModel


class ProductsGroup:
    group: FeatureModel
    users_feature: FeatureModel


class UsersGroup:
    group: FeatureModel
    users_feature: FeatureModel
    machine_assignment_feature: FeatureModel


def create_machines_group() -> MachinesGroup:
    result = MachinesGroup()

    result.group = FeatureFactory.create(name="Machines", field_name="machines")
    result.machines_feature = FeatureFactory(
        name="Machines",
        field_name="machines",
        parent=result.group,
    )
    FeatureActionFactory(feature=result.machines_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=result.machines_feature, action=ActionEnum.EDIT)

    result.devices_feature = FeatureFactory(
        name="Devices",
        field_name="devices",
        parent=result.group,
    )
    FeatureActionFactory(feature=result.devices_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=result.devices_feature, action=ActionEnum.EDIT)

    result.machine_stock_feature = FeatureFactory(
        name="Machine Stock",
        field_name="machine_stock",
        parent=result.group,
    )
    FeatureActionFactory(feature=result.machine_stock_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=result.machine_stock_feature, action=ActionEnum.EDIT)

    result.machine_planograms_feature = FeatureFactory(
        name="Machine Planograms",
        field_name="machine_planograms",
        parent=result.group,
    )
    FeatureActionFactory(
        feature=result.machine_planograms_feature, action=ActionEnum.VIEW
    )
    FeatureActionFactory(
        feature=result.machine_planograms_feature, action=ActionEnum.EDIT
    )

    result.planogram_analysis_feature = FeatureFactory(
        name="Planogram Analysis",
        field_name="planogram_analysis",
        parent=result.group,
    )
    FeatureActionFactory(
        feature=result.planogram_analysis_feature, action=ActionEnum.VIEW
    )

    result.machine_meter_readings_feature = FeatureFactory(
        name="Meter readings",
        field_name="meter_readings",
        parent=result.group,
    )
    FeatureActionFactory(
        feature=result.machine_meter_readings_feature, action=ActionEnum.VIEW
    )
    FeatureActionFactory(
        feature=result.machine_meter_readings_feature, action=ActionEnum.EDIT
    )

    return result


def create_products_group() -> ProductsGroup:
    result = ProductsGroup()

    result.group = FeatureFactory.create(name="Products", field_name="products")
    result.products_feature = FeatureFactory(
        name="Products",
        field_name="products",
        parent=result.group,
    )
    FeatureActionFactory(feature=result.products_feature, action=ActionEnum.VIEW_ALL)
    FeatureActionFactory(
        feature=result.products_feature, action=ActionEnum.VIEW_ASSIGNED
    )
    FeatureActionFactory(feature=result.products_feature, action=ActionEnum.EDIT)

    return result


def create_users_group() -> UsersGroup:
    result = UsersGroup()

    result.group = FeatureFactory.create(name="Users", field_name="users")
    result.users_feature = FeatureFactory(
        name="Users",
        field_name="users",
        parent=result.group,
    )
    FeatureActionFactory(feature=result.users_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=result.users_feature, action=ActionEnum.EDIT)

    result.machine_assignment_feature = FeatureFactory(
        name="Machine Assignment",
        field_name="machine_assignment",
        parent=result.group,
    )
    FeatureActionFactory(
        feature=result.machine_assignment_feature, action=ActionEnum.VIEW
    )
    FeatureActionFactory(
        feature=result.machine_assignment_feature, action=ActionEnum.EDIT
    )

    return result


def create_default_data():
    role_filler = RoleFactory(name="Filler")
    role_service = RoleFactory(name="Service")
    role_service_manager = RoleFactory(name="Service Manager")
    role_warehouse_manager = RoleFactory(name="Warehouse Manager")
    role_category_manager = RoleFactory(name="Category Manager")
    role_supervisor = RoleFactory(name="Supervisor")
    role_company_admin = RoleFactory(name="Company Administrator")
    role_multicompany_manager = RoleFactory(name="Multicompany Manager")
    role_superdistributor = RoleFactory(name="Superdistributor")
    role_superadmin_support = RoleFactory(name="Superadmin Support")
    role_superadmin = RoleFactory(name="Superadministrator")
    role_company_manager = RoleFactory(name="Company Manager")

    machines_group = create_machines_group()
    products_group = create_products_group()
    users_group = create_users_group()

    role_guest = RoleFactory(name="Guest")
    RolePermissionFactory(role=role_guest, feature=machines_group.machines_feature, action=ActionEnum.VIEW, permitted=False)
    RolePermissionFactory(role=role_guest, feature=machines_group.machines_feature, action=ActionEnum.EDIT, permitted=False)
    RolePermissionFactory(role=role_guest, feature=machines_group.devices_feature, action=ActionEnum.VIEW, permitted=True)
    RolePermissionFactory(role=role_guest, feature=machines_group.devices_feature, action=ActionEnum.EDIT, permitted=False)
    RolePermissionFactory(role=role_guest, feature=machines_group.machine_stock_feature, action=ActionEnum.VIEW, permitted=True)
    RolePermissionFactory(role=role_guest, feature=machines_group.machine_stock_feature, action=ActionEnum.EDIT, permitted=False)
    RolePermissionFactory(role=role_guest, feature=machines_group.machine_planograms_feature, action=ActionEnum.VIEW, permitted=True)
    RolePermissionFactory(role=role_guest, feature=machines_group.machine_planograms_feature, action=ActionEnum.EDIT, permitted=False)
    RolePermissionFactory(role=role_guest, feature=machines_group.planogram_analysis_feature, action=ActionEnum.VIEW, permitted=True)
    RolePermissionFactory(role=role_guest, feature=machines_group.planogram_analysis_feature, action=ActionEnum.EDIT, permitted=False)
    RolePermissionFactory(role=role_guest, feature=machines_group.machine_meter_readings_feature, action=ActionEnum.VIEW, permitted=True)
    RolePermissionFactory(role=role_guest, feature=machines_group.machine_meter_readings_feature, action=ActionEnum.EDIT, permitted=False)

    role_customer_support = RoleFactory(name="Customer Support")
    RolePermissionFactory(role=role_customer_support, feature=machines_group.machines_feature, action=ActionEnum.VIEW, permitted=False)
    RolePermissionFactory(role=role_customer_support, feature=machines_group.machines_feature, action=ActionEnum.EDIT, permitted=False)
    RolePermissionFactory(role=role_customer_support, feature=machines_group.devices_feature, action=ActionEnum.VIEW, permitted=True)
    RolePermissionFactory(role=role_customer_support, feature=machines_group.devices_feature, action=ActionEnum.EDIT, permitted=False)

    user1 = UserFactory(tenant_id=666, user_id=123, role=role_guest)
    UserPermissionFactory(user=user1, feature=machines_group.machines_feature, action=ActionEnum.VIEW, permitted=True)
    UserPermissionFactory(user=user1, feature=machines_group.machines_feature, action=ActionEnum.EDIT, permitted=True)
