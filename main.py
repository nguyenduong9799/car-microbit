def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_mes_dpad_controller_id_microbit_evt():
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        basic.show_arrow(ArrowNames.NORTH)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        basic.show_arrow(ArrowNames.SOUTH)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        basic.show_arrow(ArrowNames.WEST)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        basic.show_arrow(ArrowNames.EAST)
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        basic.show_string("A")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_B_DOWN:
        basic.show_string("B")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_C_DOWN:
        basic.show_string("C")
    elif control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        basic.show_string("D")
    else:
        basic.show_icon(IconNames.SMALL_HEART)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)
