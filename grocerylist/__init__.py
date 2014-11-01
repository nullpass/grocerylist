"""
TODO:


auth3p.html needs a lot -o- love

Oh yeah-- I forgot to actually enabled list_delete. doh!
    Going to move delete from checkbox to url and add deleteview
    


Audit urls
    maximize urls per page to minimize chance of user getting psudo-lost

lists.
    mark as done href (color coded by status)
    
    lists by store (not just related bubble)
    
    change listUpdate.delete_me to redirect to confirm, and confirm = ListDeleteView
    
    all lists should target=_blank
    
    
/recent/
    Not sure if I want to go the whole .logging() route or not, could probably
    just cheat and give recent by object type

/base/urls.py is a monster, keep her that way. kthnx






$ cat dir_user | tr , '\n'
['DoesNotExist'
 'Meta'
 'MultipleObjectsReturned'
 'REQUIRED_FIELDS'
 'USERNAME_FIELD'
 '__class__'
 '__delattr__'
 '__dict__'
 '__dir__'
 '__doc__'
 '__eq__'
 '__format__'
 '__ge__'
 '__getattribute__'
 '__gt__'
 '__hash__'
 '__init__'
 '__le__'
 '__lt__'
 '__module__'
 '__ne__'
 '__new__'
 '__reduce__'
 '__reduce_ex__'
 '__repr__'
 '__setattr__'
 '__sizeof__'
 '__str__'
 '__subclasshook__'
 '__weakref__'
 '_base_manager'
 '_check_column_name_clashes'
 '_check_field_name_clashes'
 '_check_fields'
 '_check_id_field'
 '_check_index_together'
 '_check_local_fields'
 '_check_m2m_through_same_relationship'
 '_check_managers'
 '_check_model'
 '_check_ordering'
 '_check_swappable'
 '_check_unique_together'
 '_default_manager'
 '_deferred'
 '_do_insert'
 '_do_update'
 '_get_FIELD_display'
 '_get_next_or_previous_by_FIELD'
 '_get_next_or_previous_in_order'
 '_get_pk_val'
 '_get_unique_checks'
 '_meta'
 '_perform_date_checks'
 '_perform_unique_checks'
 '_save_parents'
 '_save_table'
 '_set_pk_val'
 '_state'
 'check'
 'check_password'
 'clean'
 'clean_fields'
 'date_error_message'
 'date_joined'
 'delete'
 'email'
 'email_user'
 'first_name'
 'full_clean'
 'get_all_permissions'
 'get_full_name'
 'get_group_permissions'
 'get_next_by_date_joined'
 'get_next_by_last_login'
 'get_previous_by_date_joined'
 'get_previous_by_last_login'
 'get_session_auth_hash'
 'get_short_name'
 'get_username'
 'groups'
 'has_module_perms'
 'has_perm'
 'has_perms'
 'has_usable_password'
 'id'
 'is_active'
 'is_anonymous'
 'is_authenticated'
 'is_staff'
 'is_superuser'
 'isle'
 'item'
 'last_login'
 'last_name'
 'list'
 'logentry_set'
 'natural_key'
 'objects'
 'password'
 'pk'
 'prepare_database_save'
 'save'
 'save_base'
 'serializable_value'
 'set_password'
 'set_unusable_password'
 'social_auth'
 'store'
 'unique_error_message'
 'user_permissions'
 'username'
 'validate_unique']


"""
