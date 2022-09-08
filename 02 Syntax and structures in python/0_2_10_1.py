if __name__ == '__main__':
    expected_keys = {"type", "event", "visit_start",
                     "visit_end", "user_id", "product"}
    metric = {"type": "frontend",
              "event": "user_visit_create_site_page",
              "visit_start": 1622521388,
              "user_id": 342341,
              "product": "site_control_panel",
              "user_pseudo_id": 23435436344598}

    keys = set(metric.keys())

    for key in expected_keys.difference(keys):
        print("Пропущено значение " + key)

    for key in keys.difference(expected_keys):
        print("Найдено новое значение " + key)
