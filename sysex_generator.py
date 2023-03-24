def generate_sysex(address,data,mido_event=False):
    header=['41','10','42','12'] #Hex
    chktmp=0
    for i in address:
        chktmp+=int(i,base=16)
    for i in data:
        chktmp+=int(i,base=16)
    chk=(128 - (chktmp)) % 128

    sysex=[]
    for i in header:
        sysex.append(i)
    for i in address:
        sysex.append(i)
    for i in data:
        sysex.append(i)
    sysex.append(format(chk, 'x').zfill(2).upper())
    if mido_event: #Mido uses decimal
        sysex_dec=[]
        for i in sysex:
            sysex_dec.append(int(i,base=16))
        return sysex_dec
    else:
        return ' '.join(['F0']+sysex+['F7']) #Hex string
    
class efx():
    #define data values for every effect
    thru=['00','00']
    stereo_eq=['01','00']
    spectrum=['01','01']
    enhancer=['01','02']
    humanizer=['01','03']
    overdrive=['01','10']
    distortion=['01','11']
    phaser=['01','20']
    auto_wah=['01','21']
    rotary=['01','22']
    stereo_flanger=['01','23']
    step_flanger=['01','24']
    tremolo=['01','25']
    auto_pan=['01','26']
    compressor=['01','30']
    limiter=['01','31']
    hexa_chorus=['01','40']
    tremolo_chorus=['01','41']
    stereo_chorus=['01','42']
    space_d=['01','43']
    _3d_chorus=['01','44']
    stereo_delay=['01','50']
    mod_delay=['01','51']
    _3_tap_delay=['01','52']
    _4_tap_delay=['01','53']
    tm_ctrl_delay=['01','54']
    reverb=['01','55']
    gate_reverb=['01','56']
    _3d_delay=['01','57']
    _2_pitch_shifter=['01','60']
    fb_p_shifter=['01','61']
    _3d_auto=['01','70']
    _3d_manual=['01','71']
    lofi_1=['01','72']
    lofi_2=['01','73']
    #todo: series 2

class delay_macros():
    delay_1='00'
    delay_2='01'
    delay_3='02'
    delay_4='03'
    pan_delay_1='04'
    pan_delay_2='05'
    pan_delay_3='06'
    pan_delay_4='07'
    delay_to_reverb='08'
    pan_repeat='09'
    
class addresses():
    delay_macro=['40','01','50']
    delay_pre_lpf=['40','01','51']
    delay_time_center=['40','01','52']
    delay_time_ratio_left=['40','01','53']
    delay_time_ratio_right=['40','01','54']
    delay_level_center=['40','01','55']
    delay_level_left=['40','01','56']
    delay_level_right=['40','01','57']
    delay_level=['40','01','58']
    delay_feedback=['40','01','59']
    delay_send_to_reverb=['40','01','5A']

    eq_low_freq=['40','02','00']
    eq_low_gain=['40','02','01']
    eq_high_freq=['40','02','02']
    eq_high_gain=['40','02','03']
    
    efx_type=['40','03','00']

    efx_on_1=['40','41','22']
    efx_on_2=['40','42','22']
    efx_on_3=['40','43','22']
    efx_on_4=['40','44','22']
    efx_on_5=['40','45','22']
    efx_on_6=['40','46','22']
    efx_on_7=['40','47','22']
    efx_on_8=['40','48','22']
    efx_on_9=['40','49','22']
    efx_on_10=['40','4A','22']
    efx_on_11=['40','4B','22']
    efx_on_12=['40','4C','22']
    efx_on_13=['40','4D','22']
    efx_on_14=['40','4E','22']
    efx_on_15=['40','4F','22']
    
    efx_params_start=['40','03','03']
    
    efx_param_1=['40','03','03']
    efx_param_2=['40','03','04']
    efx_param_3=['40','03','05']
    efx_param_4=['40','03','06']
    efx_param_5=['40','03','07']
    efx_param_6=['40','03','08']
    efx_param_7=['40','03','09']
    efx_param_8=['40','03','0A']
    efx_param_9=['40','03','0B']
    efx_param_10=['40','03','0C']
    efx_param_11=['40','03','0D']
    efx_param_12=['40','03','0E']
    efx_param_13=['40','03','0F']
    efx_param_14=['40','03','10']
    efx_param_15=['40','03','11']
    efx_param_16=['40','03','12']
    efx_param_17=['40','03','13']
    efx_param_18=['40','03','14']
    efx_param_19=['40','03','15']
    efx_param_20=['40','03','16']

    efx_reverb_send=['40','03','17']
    efx_chorus_send=['40','03','18']
    efx_delay_send=['40','03','19']

    efx_control_source_1=['40','03','1B']
    efx_control_depth_1=['40','03','1C']
    efx_control_source_2=['40','03','1D']
    efx_control_depth_2=['40','03','1E']
    efx_send_eq_switch=['40','03','1F']








    
