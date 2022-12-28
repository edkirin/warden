INSERT INTO public.feature_groups (id, name, field_name)
    VALUES
        (1, 'Machines', 'machines'),
        (2, 'Users', 'users'),
        (3, 'Events', 'events')
;


INSERT INTO public.features (id, name, feature_group_id, field_name)
    VALUES
        (1, 'Machines', 1, 'machines'),
        (2, 'Devices', 1, 'devices'),
        (3, 'Machine Stock', 1, 'machine_stock'),
        (4, 'Machine Planograms', 1, 'machine_planograms'),
        (5, 'Planogram Analysis', 1, 'planogram_analysis'),
        (6, 'Meter Readings', 1, 'meter_readings'),
        (7, 'Fiscal Setup', 1, 'fiscal_setup'),
        (8, 'Users', 2, 'users'),
        (9, 'Machine Assignment', 2, 'machine_assignment'),
        (10, 'Event List', 3, 'event_list')
;


INSERT INTO public.roles (id, name)
    VALUES
        (1, 'Guest'),
        (2, 'Customer Support'),
        (3, 'Filler'),
        (4, 'Service'),
        (5, 'Service Manager'),
        (6, 'Warehouse Manager'),
        (7, 'Category Manager'),
        (8, 'Supervisor'),
        (9, 'Company Administrator'),
        (10, 'Company Manager'),
        (11, 'Multicompany Manager'),
        (12, 'Superdistributor'),
        (13, 'Superadmin Support'),
        (14, 'Superadministrator')
;


INSERT INTO public.role_permissions (feature_id, action, permitted)
    VALUES
        (1, 'VIEW', true)
;
