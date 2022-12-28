from service.api.enums import ActionEnum
from service.factories import FeatureFactory, RoleFactory, FeatureActionFactory


def create_default_data():
    role_guest = RoleFactory(name="Guest")
    role_customer_support = RoleFactory(name="Customer Support")
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

    machines_group = FeatureFactory.create(name="Machines", field_name="machines")
    machines_machines_feature = FeatureFactory(
        name="Machines",
        field_name="machines",
        parent=machines_group,
    )
    FeatureActionFactory(feature=machines_machines_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=machines_machines_feature, action=ActionEnum.EDIT)

    machines_devices_feature = FeatureFactory(
        name="Devices",
        field_name="devices",
        parent=machines_group,
    )
    FeatureActionFactory(feature=machines_devices_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=machines_devices_feature, action=ActionEnum.EDIT)

    machines_machine_stock_feature = FeatureFactory(
        name="Machine Stock",
        field_name="machine_stock",
        parent=machines_group,
    )
    FeatureActionFactory(feature=machines_machine_stock_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=machines_machine_stock_feature, action=ActionEnum.EDIT)

    machines_machine_planograms_feature = FeatureFactory(
        name="Machine Planograms",
        field_name="machine_planograms",
        parent=machines_group,
    )
    FeatureActionFactory(feature=machines_machine_planograms_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=machines_machine_planograms_feature, action=ActionEnum.EDIT)

    machines_machine_planogram_analysis_feature = FeatureFactory(
        name="Planogram Analysis",
        field_name="planogram_analysis",
        parent=machines_group,
    )
    FeatureActionFactory(feature=machines_machine_planogram_analysis_feature, action=ActionEnum.VIEW)

    machines_machine_meter_readings_feature = FeatureFactory(
        name="Meter readings",
        field_name="meter_readings",
        parent=machines_group,
    )
    FeatureActionFactory(feature=machines_machine_meter_readings_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=machines_machine_meter_readings_feature, action=ActionEnum.EDIT)

    products_group = FeatureFactory.create(name="Products", field_name="products")
    products_feature = FeatureFactory(
        name="Products",
        field_name="products",
        parent=products_group,
    )
    FeatureActionFactory(feature=products_feature, action=ActionEnum.VIEW_ALL)
    FeatureActionFactory(feature=products_feature, action=ActionEnum.VIEW_ASSIGNED)
    FeatureActionFactory(feature=products_feature, action=ActionEnum.EDIT)

    users_group = FeatureFactory.create(name="Users", field_name="users")
    users_users_feature = FeatureFactory(
        name="Users",
        field_name="users",
        parent=users_group,
    )
    FeatureActionFactory(feature=users_users_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=users_users_feature, action=ActionEnum.EDIT)

    users_machine_assignment_feature = FeatureFactory(
        name="Machine Assignment",
        field_name="machine_assignment",
        parent=users_group,
    )
    FeatureActionFactory(feature=users_machine_assignment_feature, action=ActionEnum.VIEW)
    FeatureActionFactory(feature=users_machine_assignment_feature, action=ActionEnum.EDIT)
