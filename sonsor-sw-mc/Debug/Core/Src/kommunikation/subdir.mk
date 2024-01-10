################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/kommunikation/interface_receive_handler.c \
../Core/Src/kommunikation/sensor_send_interface.c \
../Core/Src/kommunikation/uart_processor.c 

OBJS += \
./Core/Src/kommunikation/interface_receive_handler.o \
./Core/Src/kommunikation/sensor_send_interface.o \
./Core/Src/kommunikation/uart_processor.o 

C_DEPS += \
./Core/Src/kommunikation/interface_receive_handler.d \
./Core/Src/kommunikation/sensor_send_interface.d \
./Core/Src/kommunikation/uart_processor.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/kommunikation/%.o Core/Src/kommunikation/%.su Core/Src/kommunikation/%.cyclo: ../Core/Src/kommunikation/%.c Core/Src/kommunikation/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F411xE -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src-2f-kommunikation

clean-Core-2f-Src-2f-kommunikation:
	-$(RM) ./Core/Src/kommunikation/interface_receive_handler.cyclo ./Core/Src/kommunikation/interface_receive_handler.d ./Core/Src/kommunikation/interface_receive_handler.o ./Core/Src/kommunikation/interface_receive_handler.su ./Core/Src/kommunikation/sensor_send_interface.cyclo ./Core/Src/kommunikation/sensor_send_interface.d ./Core/Src/kommunikation/sensor_send_interface.o ./Core/Src/kommunikation/sensor_send_interface.su ./Core/Src/kommunikation/uart_processor.cyclo ./Core/Src/kommunikation/uart_processor.d ./Core/Src/kommunikation/uart_processor.o ./Core/Src/kommunikation/uart_processor.su

.PHONY: clean-Core-2f-Src-2f-kommunikation

