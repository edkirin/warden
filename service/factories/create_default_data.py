from service.factories import FeatureFactory, FeatureGroupFactory, RoleFactory


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

    machines_group = FeatureGroupFactory.create(name="Machines", field_name="machines")
    machines_machines_feature = FeatureFactory(
        name="Machines",
        field_name="machines",
        feature_group=machines_group,
    )
    machines_devices_feature = FeatureFactory(
        name="Devices",
        field_name="devices",
        feature_group=machines_group,
    )
    machines_machine_stock_feature = FeatureFactory(
        name="Machine Stock",
        field_name="machine_stock",
        feature_group=machines_group,
    )
    machines_machine_planograms_feature = FeatureFactory(
        name="Machine Planograms",
        field_name="machine_planograms",
        feature_group=machines_group,
    )
    machines_machine_planogram_analysis_feature = FeatureFactory(
        name="Planogram Analysis",
        field_name="planogram_analysis",
        feature_group=machines_group,
    )
    machines_machine_meter_readings_feature = FeatureFactory(
        name="Meter readings",
        field_name="meter_readings",
        feature_group=machines_group,
    )

    products_group = FeatureGroupFactory.create(name="Products", field_name="products")
    products_feature = FeatureFactory(
        name="Products",
        field_name="products",
        feature_group=products_group,
    )

    users_group = FeatureGroupFactory.create(name="Users", field_name="users")
    users_users_feature = FeatureFactory(
        name="Users",
        field_name="users",
        feature_group=users_group,
    )
    users_machine_assignment_feature = FeatureFactory(
        name="Machine Assignment",
        field_name="machine_assignment",
        feature_group=users_group,
    )
